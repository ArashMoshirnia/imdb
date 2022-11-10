from django.http import HttpResponse
from django.shortcuts import render, redirect

from movies.models import Movie
from movies.forms import MovieForm


def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        context = {
            "movies": movies,
            "user": "Arash",
            "is_valid": True
        }
        return render(request, 'movies/movies_list.html', context=context)

    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('movies_list')

        return movie_add(request, form)


def movie_detail(request, pk):
    return HttpResponse(f'<h1>This is movie {pk}</h1>')


def movie_add(request, movie_form=None):
    if not movie_form:
        movie_form = MovieForm()
    return render(request, 'movies/movie_add.html', context={'form': movie_form})
