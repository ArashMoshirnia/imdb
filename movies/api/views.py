from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
