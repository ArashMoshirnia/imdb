from django.urls import path

from .views import movies_list_api

urlpatterns = [
    path('movies/', movies_list_api, name='movies_list_api'),
]
