from celery import Celery

app = Celery('crawler', broker='amqp://guest@localhost//')