from celery import Celery

app = Celery('crawler', broker='amqp://guest@localhost//')

DB_DESCRIPTOR = "sqlite:///debug.db"

PAGINATOR_REGEXP = ":PAGINATOR"

