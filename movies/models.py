from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# from django.core.exceptions import ValidationError
# from django.db.models.manager import BaseManager
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _

from comments.models import AbstractComment
# from movies.signals import movie_created
from users.models import User


class ValidManager(models.Manager):
    def get_queryset(self):
        return super(ValidManager, self).get_queryset().filter(is_valid=True)


class HorrorManager(models.Manager):
    def get_queryset(self):
        return super(HorrorManager, self).get_queryset().filter(genres__title__in=['Horror', 'Thriller'])


class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    is_valid = models.BooleanField(default=True, verbose_name=_('Is Valid'))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Time'))
    modified_time = models.DateTimeField(auto_now=True, verbose_name=_('Modified Time'))

    objects = models.Manager()
    valid_objects = ValidManager()

    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Crew(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=MALE)
    avatar = models.ImageField(upload_to='crew/avatars/', null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='movies/avatars/', null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    crew = models.ManyToManyField(Crew, through='MovieCrew', related_name='movies')
    view_count = models.IntegerField(default=0)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    valid_objects = ValidManager()
    horror_objects = HorrorManager()

    def get_description(self):
        return self.description.lower()

    @property
    def average_rating(self):
        rate = self.ratings.all().aggregate(avg=Avg('rate'))
        return rate.get('avg') or 1

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.description = self.description.capitalize()
        print('In movie save')
        super(Movie, self).save(*args, **kwargs)
        print('After save')
        # movie_created.send(self.__class__)

    # def clean(self):
    #     raise ValidationError('Not good')


class MovieCrew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_crew')
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name='movie_crew')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='movie_crew')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('movie', 'crew', 'role')


class MovieComment(AbstractComment):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class CrewComment(AbstractComment):
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_ratings')
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=('user', 'movie'), name='unique_user_movie')]
