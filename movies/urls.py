from django.urls import path

from .views import movies_list, movie_detail, movie_add

urlpatterns = [
    path('movies/', movies_list, name='movies_list'),
    path('movies/<int:pk>', movie_detail, name='movie_detail'),

    path('movies/add/', movie_add, name='movie_add'),
]
