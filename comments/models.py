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

