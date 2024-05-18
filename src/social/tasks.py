from celery import shared_task

from .models import SocialTypes, Social


@shared_task
def test():
    print("Job is running")
    for social in Social.objects.all():
        print(social.link)