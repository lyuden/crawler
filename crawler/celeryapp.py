from celery import Celery

from datetime import timedelta


app = Celery('crawler', broker='amqp://guest@localhost//')

app.conf.CELERYBEAT_SCHEDULE = {
    'stage_one': {
        'task': 'form_depth_zero_urls_task',
        'schedule': timedelta(seconds=10),
    },
    'stage_two': {
        'task': 'generate_depth_zero_tasks',
        'schedule': timedelta(seconds=20),
    },
}
