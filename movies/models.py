from django.conf import settings
from django.db import models
# from django.core.exceptions import ValidationError
# from django.db.models.manager import BaseManager
from comments.models import AbstractComment
from users.models import User

class ValidManager(models.Manager):
    def get_queryset(self):
        return super(ValidManager, self).get_queryset().filter(is_valid=True)


class HorrorManager(models.Manager):
    def get_queryset(self):
        return super(HorrorManager, self).get_queryset().filter(genres__title__in=['Horror', 'Thriller'])


class Genre(models.Model):
    title = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

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
        (MALE, 'Male'),
        (FEMALE, 'Female')
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

    def __str__(self):
        return self.title

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
