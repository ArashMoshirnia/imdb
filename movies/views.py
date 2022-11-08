from django.http import HttpResponse
from django.shortcuts import render, redirect

from movies.models import Movie
from movies.forms import MovieForm


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


def movie_add(request, movie_form=None):
    if request.method == 'GET':
        if not movie_form:
            movie_form = MovieForm()
        return render(request, 'movies/movie_add.html', context={'form': movie_form})

    elif request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()

            # title = form.cleaned_data.get('title')
            # description = form.cleaned_data.get('description')
            # release_date = form.cleaned_data.get('release_date')
            # avatar = form.cleaned_data.get('avatar')
            #
            # Movie.objects.create(
            #     title=title,
            #     description=description,
            #     release_date=release_date,
            #     avatar=avatar
            # )

            # Redirect
            return redirect('movies_list')

        request.method = 'GET'
        return movie_add(request, form)
