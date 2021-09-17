from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Movie
from .forms import MovieForm
from django.core.paginator import Paginator


@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    paginator = Paginator(movies, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            if not movie.image:
                movie.image = 'images/no_image.png'
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/form.html', context)


@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save()
            if not movie.image:
                movie.image = 'images/no_image.png'
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/form.html', context)


@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movies:index')
