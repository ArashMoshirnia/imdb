import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imdb.settings')
app = Celery('imdb')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def debug_task(num):
    print(f'Hello world: {num}')
    raise Exception('Wrong')
