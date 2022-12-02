from django.urls import path

from .views import movies_list_api, MovieListAPIView

urlpatterns = [
    path('movies/', MovieListAPIView.as_view(), name='movies_list_api'),
]
