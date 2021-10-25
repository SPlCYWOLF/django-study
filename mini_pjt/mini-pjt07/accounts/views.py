from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('community:index')


def profile(request, username):
    target = get_object_or_404(get_user_model(), username=username)
    context = {
        'target': target,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, username):
    if request.user.is_authenticated:
        target = get_object_or_404(get_user_model(), username=username)
        if request.user != target:
            if target.followings.filter(username=request.user).exists():
                target.followings.remove(request.user)
            else:
                target.followings.add(request.user)
        return redirect('accounts:profile', username)
    return redirect('accounts:login')