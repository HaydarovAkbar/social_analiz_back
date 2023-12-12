from django.conf import settings
import requests
import time

from config import celery_app
from social.models import SocialPost, Social, SocialTypes, Organization, SocialPostStats
from utils.models import State
from .bot.utils import tg_parse


def get_stats(integration_id):
    url = settings.LIVEDONE_POST_URL.replace("ID", integration_id) + "?access_token=" + settings.LIVEDONE_TOKEN
    responce = requests.get(url).json()['response']
    return responce


def get_followers(social_type, integration_id):
    url = settings.LIVEDONE_ACCOUNTS_URL + "?access_token=" + settings.LIVEDONE_TOKEN + "&social=" + social_type + "&id=" + integration_id
    responce = requests.get(url).json()['response']
    return responce


@celery_app.task
def web_scrapping_tg(organization):
    try:
        tg_channel = Social.objects.get(organization=organization, social_type=SocialTypes.objects.get(attr="telegram"))
        for post in SocialPost.objects.filter(organization=organization,
                                              social_type=SocialTypes.objects.get(attr="telegram")).order_by(
            '-post_date')[
                    :settings.TG_PARSE_MSG_COUNT]:
            parser = tg_parse(post.post_id, tg_channel.link)
            if parser:
                views, post_date = parser
                if SocialPostStats.objects.filter(post=post, stat_date__year=post_date.year,
                                                  stat_date__month=post_date.month,
                                                  stat_date__day=post_date.day).exists():
                    SocialPostStats.objects.filter(post=post, stat_date__year=post_date.year,
                                                   stat_date__month=post_date.month,
                                                   stat_date__day=post_date.day).update(views=views)
                else:
                    SocialPostStats.objects.create(post=post, views=views)
            time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False


@celery_app.task
def parsing_web_tg():
    print("Hello this is task")
    for organ in Organization.objects.filter(state=State.objects.first()):
        web_scrapping_tg(organ)


# Compare this snippet
@celery_app.task
def update_social_stats():
    try:
        for social in Social.objects.filter(state=State.objects.first()):
            if social.social_type.attr == "telegram":
                continue
            stats = get_stats(social.integration_id)
            if stats:
                for post_stats in stats:
                    post = SocialPost.objects.filter(post_id=post_stats['id']).first()
                    if post:
                        get_follower_response = get_followers(social.social_type.attr, social.integration_id)
                        if SocialPostStats.objects.filter(post=post).exists():
                            SocialPostStats.objects.filter(post=post.update(
                                reactions=post_stats["reactions"].get('reactions', 0),
                                views=post_stats.get('video_views', 0),
                                comments=post_stats["reactions"].get('comments', 0),
                                likes=post_stats["reactions"].get('likes', 0),
                                reposts=post_stats["reactions"].get('reposts', 0),
                                # dislikes = post_stats["dislikes"].get('dislikes', 0),
                                followers=get_follower_response['stat']['followers']
                            ))
                        else:
                            SocialPostStats.objects.create(post=post,
                                                           reactions=post_stats["reactions"].get('reactions', 0),
                                                           views=post_stats.get('video_views', 0),
                                                           comments=post_stats["reactions"].get('comments', 0),
                                                           likes=post_stats["reactions"].get('likes', 0),
                                                           reposts=post_stats["reactions"].get('reposts', 0),
                                                           social=social,

                                                           followers=get_follower_response['stat']['followers']
                                                           )
            time.sleep(0.5)
        return True
    except Exception as e:
        print(e)
        return False
