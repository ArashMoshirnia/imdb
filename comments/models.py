from django.conf import settings
from django.db import models


class AbstractComment(models.Model):
    CREATED = 10
    APPROVED = 20
    REJECTED = 30
    DELETED = 40
    STATUS_CHOICES = (
        (CREATED, 'Created'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (DELETED, 'Deleted')
    )

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='%(class)ss')
    comment_body = models.TextField()

    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=CREATED)
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='validated_%(class)ss')

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Proxy example

# class ValidManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_valid=True)
#
#
# class NameModel(models.Model):
#     name = models.CharField(max_length=100)
#     is_valid = models.BooleanField(default=True)
#
#     class Meta:
#         proxy = True
#
#
# class ValidName(NameModel):
#     objects = ValidManager()
#
#
# class OrderedName(NameModel):
#     class Meta:
#         ordering = ('name', )


class CurrencyExchangeRate(models.Model):
    currency_from = models.CharField(max_length=4)
    currency_to = models.CharField(max_length=4)
    rate = models.FloatField()


# CurrencyExchangeRate(currency_from='USD', currency_to='IRR', rate=400000)
# CurrencyExchangeRate(currency_from='USD', currency_to='EUR', rate=0.99)


# Django command to retrieve and save all CurrencyExchangeRates to a redis Hashmap
# ex = {
#     "USD/IRR": 400000,
#     "USD/EUR": 0.99
# }

# Function that receives two currency codes and return the exchange rate from redis

# Hashmap commands: HSET, HGET, HGETALL
