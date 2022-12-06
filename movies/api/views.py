from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets

from movies.models import Movie
from movies.api.serializers import MovieSerializer


@api_view(['GET', 'POST'])
def movies_list_api(request):
    if request.method == 'GET':
        movies = Movie.valid_objects.prefetch_related('genres', 'crew')
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
    serializer_class = MovieSerializer
    # parser_classes = [JSONParser, MultiPartParser]
    # renderer_classes = [JSONRenderer]

    # def get_queryset(self):
    #     a_month_ago = timezone.now().date() - timezone.timedelta(days=30)
    #     queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
    #     if self.request.method == 'GET':
    #         queryset = queryset.filter(release_date__gte=a_month_ago)
    #
    #     return queryset


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
    serializer_class = MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
    serializer_class = MovieSerializer

    @method_decorator(cache_page(15))
    def list(self, request, *args, **kwargs):
        return super(MovieViewSet, self).list(request, *args, **kwargs)

    @action(methods=['POST'], detail=False, url_path='movie_rate')
    def rate(self, request, *args, **kwargs):
        return Response({'result': f'rate submitted for movie'})

