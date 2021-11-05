from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Movie
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    movies = Movie.objects.order_by("pk")
    paginator = Paginator(movies, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "movies": page_obj,
    }
    return render(request, "movies/index.html", context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        "movie": movie,
    }
    return render(request, "movies/detail.html", context)


def recommended(request):
    return render(request, "movies/recommended.html")
