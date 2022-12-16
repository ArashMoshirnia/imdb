import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imdb.settings')
app = Celery('imdb')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.task_routes = {'users.tasks.*': {'queue': 'users'}}
app.conf.beat_schedule = {
    # 'my_periodic_task': {
    #     'task': 'users.tasks.my_periodic_task',
    #     'schedule': crontab(minute='*', hour='*'),
    # },
    'temp_task': {
        'task': 'users.tasks.temp_task',
        'schedule': crontab(minute='*/5', hour='*'),
    },
}


@app.task
def debug_task(num):
    print(f'Hello world: {num}')
    raise Exception('Wrong')
