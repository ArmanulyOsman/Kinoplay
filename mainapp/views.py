from django.shortcuts import render
from mainapp.models import Movie, Director


def index(request):
    movies = Movie.objects.all()

    return render(request, 'index.html', {"movies": movies})


def director(request, id):
    director_movies = Movie.objects.filter(director=Director.objects.get(id=id))
    print(director_movies)
    return render(request, 'director.html', {"movies": director_movies, "director":Director.objects.get(id=id)})


def show(request, id):
    return render(request, 'show.html', {"movie": Movie.objects.get(id=id)})
