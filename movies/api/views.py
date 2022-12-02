from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics
from django.utils import timezone

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


class MovieListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
    serializer_class = MovieSerializer

    def get_queryset(self):
        a_month_ago = timezone.now().date() - timezone.timedelta(days=30)
        queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
        if self.request.method == 'GET':
            queryset = queryset.filter(release_date__gte=a_month_ago)

        return queryset

    def get_serializer_class(self):
        return MovieSerializer

    def get(self, request, *args, **kwargs):
        # movies = Movie.valid_objects.prefetch_related('genres', 'crew')
        # serializer = MovieSerializer(movies, many=True)
        # return Response(serializer.data)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # serializer = MovieSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)

        return self.create(request, *args, **kwargs)
