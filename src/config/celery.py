from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'run-task-at-8am': {
        'task': 'app.tasks.test',
        'schedule': crontab(hour=8, minute=0),
    },
    'run-task-at-12pm': {
        'task': 'app.tasks.test2',
        'schedule': crontab(hour=12, minute=0),
    },
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")