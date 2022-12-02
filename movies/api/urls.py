from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import movies_list_api, MovieListAPIView, MovieDetailAPIView, MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')


urlpatterns = [
    # path('movies/', MovieListAPIView.as_view(), name='movies_list_api'),
    # path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movies_detail_api'),
    # path('movies/<int:pk>/rate/', MovieDetailAPIView.as_view(), name='movies_detail_api'),

    # path('movies/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movies_list_api'),
    # path('movies/<int:pk>/', MovieViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
    # ), name='movies_detail_api'),
]

urlpatterns += router.urls
