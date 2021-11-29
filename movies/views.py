from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    # output = ", ".join([m.title for m in movies]) #

    # # SELECT * FROM movies_movie #possible outputs
    # Movie.objects.filter(release_year=1994)
    # #SELECT * FROM movies_movie WHERE release_year = 1994
    # Movies.objects.get(id=1)

    # return HttpResponse("- Hello there! \n - General Kenobi!") #pure print

    output = render(request, "movies/index.html", {'movies': movies})

    return HttpResponse(output)


def detail(request, movie_id):
    # Movie
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
