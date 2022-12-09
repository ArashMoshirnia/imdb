from movies.api.serializers import MovieSerializer
from movies.models import Movie


class MovieSerializerV2(MovieSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'avatar', 'view_count',
                  'created_time', 'is_released', 'genres', 'movie_crew')

    def validate_title(self, attr):
        return attr.upper()
