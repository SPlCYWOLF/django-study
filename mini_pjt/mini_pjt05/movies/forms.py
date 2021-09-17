from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.Textarea(
            attrs={
                'class': 'my-title form-control',
                'placeholder': '제목을 입력해주세요',
                'minlength': 1,
                'maxlength': 100,
                'rows': 1,
                'autofocus': True,
            }
        )
    )
    overview = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-title form-control',
                'placeholder': '내용을 입력해주세요',
                'minlength': 10,
                'maxlength': 1000,
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'
