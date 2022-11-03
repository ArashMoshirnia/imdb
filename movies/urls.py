from django.urls import path

from .views import movies_list, movie_detail, form_post, form_view

urlpatterns = [
    path('movies/', movies_list, name='movies_list'),
    path('movies/<int:pk>', movie_detail, name='movie_detail'),
    path('form/', form_view, name='form_view'),
    path('form/post/', form_post, name='form_post'),
]
