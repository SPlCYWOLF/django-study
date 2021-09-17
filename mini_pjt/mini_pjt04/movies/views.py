from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.
def index(request):

    movies = Movie.objects.all()[::-1]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')
    movie = Movie(title=title, overview=overview, poster_path=poster_path)
    movie.save()
    # return render(request, 'movies/create.html')
    return redirect('movies:detail', movie.pk)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context ={
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')

    movie.title = title
    movie.overview = overview
    movie.poster_path = poster_path
    movie.save()

    return redirect('movies:detail', movie_pk)


def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie_pk)
    
