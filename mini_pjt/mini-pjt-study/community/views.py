from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
# Create your views here.

def create(request):
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


def detail(request, community_pk):
    review = get_object_or_404(Review, pk=community_pk)
    context = {
        'review': review,
    }
    return render(request, 'community/detail.html', context)


def update(request, community_pk):
    review = get_object_or_404(Review, pk=community_pk)
    if request.method == 'POST':
        form = ReviewForm(data=request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
    }
    return render(request, 'community/update.html', context)


def delete(request, community_pk):
    review = get_object_or_404(Review, pk=community_pk)
    review.delete()
    return redirect('community:index')