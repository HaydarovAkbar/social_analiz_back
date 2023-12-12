from config import celery_app
from social.models import SocialPost, Social, SocialTypes, Organization, SocialPostStats
from utils.models import State
import requests


@celery_app.task
def web_scrapping(organization):
    groupmember = GroupMember.objects.get(id=groupmember_id)
    url = f"https://leetcode-stats-api.herokuapp.com/{groupmember.username}"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        DailyCheckResult.objects.create(
            member=groupmember,
            result=data
        )


@celery_app.task
def parsing_web_tg():
    print("Hello this is task")
    for organ in Organization.objects.filter(state=State.objects.first()):
        web_scrapping(organ)