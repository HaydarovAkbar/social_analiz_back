from django.conf import settings
import requests
import time

from config import celery_app
from social.models import SocialPost, Social, SocialTypes, Organization, SocialPostStats
from utils.models import State
from .bot.utils import tg_parse


def get_stats(integration_id):
    url = settings.LIVEDONE_URL.replace("ID", integration_id) + "?access_token=" + settings.LIVEDONE_TOKEN
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
    for social in Social.objects.filter(state=State.objects.first()):
        if social.social_type.attr == "telegram":
            continue
        stats = get_stats(social.integration_id)
        if stats:
            for post_stats in stats:
                post = SocialPost.objects.filter(post_id=post_stats['id']).first()
                if post:
                    if SocialPostStats.objects.filter(post=post, stat_date__year=post_stats['date'].year,
                                                      stat_date__month=post_stats['date'].month,
                                                      stat_date__day=post_stats['date'].day).exists():
                        SocialPostStats.objects.filter(post=post, stat_date__year=post_stats['date'].year,
                                                       stat_date__month=post_stats['date'].month,
                                                       stat_date__day=post_stats['date'].day).update(
                            views=post_stats['views'])
                    else:
                        SocialPostStats.objects.create(post=post, views=post_stats['views'],
                                                       stat_date=post_stats['date'])
        time.sleep(0.5)
    return True
