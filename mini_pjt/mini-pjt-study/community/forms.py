from django.forms.forms import Form
from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = '__all__'