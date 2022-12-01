from django.urls import path, include

from .views import movies_list, movie_detail, movie_add, movie_edit, movie_delete

urlpatterns = [
    path('movies/', movies_list, name='movies_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),

    path('movies/<int:pk>/edit/', movie_edit, name='movie_edit'),
    path('movies/<int:pk>/delete/', movie_delete, name='movie_delete'),
    path('movies/add/', movie_add, name='movie_add'),

    path('api/', include('movies.api.urls'))
]
