from django.db.models import fields
from community import models
from .models import Review, Comment
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'like_users')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)