import logging

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal

from movies.models import Movie

movie_created = Signal()


@receiver(post_save, sender=Movie)
def created_movie_signal(sender, **kwargs):
    logger = logging.getLogger('movies')
    logger.info('New movie is created')


@receiver(post_save, sender=Movie)
def created_movie_signal(sender, **kwargs):
    print('New movie')


@receiver(pre_save, sender=Movie)
def created_movie_signal(sender, instance, **kwargs):
    print(f'About to save movie: {instance.title}')
