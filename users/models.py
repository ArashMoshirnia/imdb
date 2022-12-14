from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

# Authentication -> Who are you? -> User recognition
# Authorization -> What can you do? -> User permissions

# django_user


class User(AbstractUser):
    # users_user
    phone_number = models.CharField(unique=True, max_length=12)
    # phone_number = models.PositiveBigIntegerField(unique=True, validators=[
    #         RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.', 'invalid')
    # ])
    address = models.TextField(blank=True)
    birthday = models.DateField(null=True)
    avatar = models.ImageField(null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone_number"]


# class UserManager(BaseUserManager):
#     def create_user(self, email, password, *args, **kwargs):
#         pass
#
#     def create_superuser(self, email, password, *args, **kwargs):
#         pass
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     address = models.TextField()
#     birthday = models.DateField()
#     avatar = models.ImageField()
