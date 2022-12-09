from rest_framework.routers import DefaultRouter

from movies.api.v2.views import MovieViewSetV2

router = DefaultRouter()
router.register(r'movies', MovieViewSetV2, basename='movies')

urlpatterns = router.urls
