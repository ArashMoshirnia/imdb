from django.urls import path
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter

from .views import movies_list_api, MovieListAPIView, MovieDetailAPIView, MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')

movies_list = MovieViewSet.as_view({'get': 'list', 'post': 'create'})
movies_detail = MovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                      'patch': 'partial_update', 'delete': 'destroy'})

urlpatterns = [
    # path('movies/', MovieListAPIView.as_view(), name='movies_list_api'),
    # path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movies_detail_api'),
    # path('movies/<int:pk>/rate/', MovieDetailAPIView.as_view(), name='movies_detail_api'),

    # path('movies/', cache_page(15)(movies_list), name='movies_list_api'),
    # path('movies/<int:pk>/', movies_detail, name='movies_detail_api'),
]

urlpatterns += router.urls
