from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def movies_list(request):
    movies = Movie.objects.all()[:8]
    context = {
        "movies": movies,
        "user": "Arash",
        "is_valid": True
    }
    return render(request, 'movies/movies_list.html', context=context)


def movie_detail(request, pk):
    return HttpResponse(f'<h1>This is movie {pk}</h1>')


def form_view(request):
    pass


def form_post(request):
    pass
