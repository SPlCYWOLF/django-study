from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
# Create your views here.


@require_http_methods(['GET', 'POST'])
@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/com_form.html', context)
    

@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review,
        'form': form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def comment_create(request, review_pk):
    
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
        return redirect('community:detail', review_pk)
    return redirect('accounts:login')


@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)
        return redirect('community:detail', review_pk)
    return redirect('accounts:login')
    
    