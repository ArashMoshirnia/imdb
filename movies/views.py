from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie
from movies.forms import TempForm


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
    return render(request, 'movies/temp.html')


def form_post(request):
    form = TempForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        return HttpResponse('Done')

    return HttpResponse(str(form.errors))


# def form_post(request):
#     name = request.POST.get('name')
#     password = request.POST.get('password')
#     age = request.POST.get('age')
#
#     if not name or not password or not age:
#         return HttpResponse('Data can not be empty', status=400)
#
#     if int(age) < 18:
#         return HttpResponse('User not allowed', status=400)
#
#     if len(password) < 8:
#         return HttpResponse('Password is too weak', status=400)
#
#     return HttpResponse('Done')
