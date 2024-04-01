from django.shortcuts import render
from mainapp.models import Movie, Director, Category


context = {
    "categories": Category.objects.all()
}


def index(request):
    movies = Movie.objects.all()
    context["movies"] = movies

    return render(request, 'index.html', context)


def director(request, id):
    director_movies = Movie.objects.filter(director=Director.objects.get(id=id))
    context["movies"] = director_movies
    context["director"] = Director.objects.get(id=id)

    return render(request, 'director.html', context)


def show(request, id):
    context["movie"] = Movie.objects.get(id=id)

    return render(request, 'show.html', context)


def categories(request, id):
    context["movies"] = Movie.objects.filter(category=Category.objects.get(id=id))

    return render(request, 'category.html', context)

