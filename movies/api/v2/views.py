from movies.api.v2.serializers import MovieSerializerV2
from movies.api.views import MovieViewSet


class MovieViewSetV2(MovieViewSet):
    pagination_class = None
    serializer_class = MovieSerializerV2

    def paginate_queryset(self, queryset):
        return None
