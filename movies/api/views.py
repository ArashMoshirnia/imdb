from django.http import JsonResponse

from movies.models import Movie


def movies_list_api(request):
    movies = Movie.valid_objects.prefetch_related('genres', 'crew')
    movie_objects = []
    for movie in movies:
        movie_objects.append(
            {
                'id': movie.id,
                'title': movie.title,
                'description': movie.description,
                'release_date': movie.release_date.strftime('%Y-%m-%d') if movie.release_date else None,
                'genres': [{'id': genre.id, 'title': genre.title} for genre in movie.genres.all()]
            }
        )

    # movie_objects = json.dumps(movie_objects)

    return JsonResponse(movie_objects, safe=False)