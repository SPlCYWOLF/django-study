유저와 유저간의 M:N 관계를 갖는 테이블을 만들기 위해 (팔로우)

먼저 User 에 클래스 변수를 추가적으로 선언할 필요가 있다.

하지만 기존에 장고 내장 User 를 써버리니까 불가능해서, 직접 쓰고있던 User를 상속받아서 필드를 추가하는식으로 간다.

ex.:

```python
# accounts/models.py
class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    age = models.PositiveIntegerField()
```

```python
# community/models.py
class Review(models.Model):
    ...
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
	
    def __str__(self):
        return f'{self.title}'
    
class Comment(models.Model):
    author = models.ForeignKey(serttings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.content}'
```



하지만 이런식으로 유저를 확장하면, 

아래와같이 수정 필요

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'
```

또한,  기존의 `UserCreationForm` 을 customize 버전으로 바꿀 필요있다.

```python
# accounts/forms.py
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'age',)
        
# community/forms.py
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # 사용자에게 보여주고 is_valid() 에서 검증할 필드들
        fields = ('title', 'content', 'rank',)
 
class CommentForm(forms.ModelForm):
    content = forms.CharField(
    	min_length=2,
        max_length=200,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    class Meta:
        model = Comment
        # 사용자에게 보여주고 is_valid() 에서 검증할 필드들
        fields = ('content',)
```







## 꿀팁

1. `review.content|linebreaksbr` => 사용자 입력때 enter 누르면 그대로 반영
2. `{% empty %}` => 아무것도 없을때 표시할 내용
3. `django-seed`
   - pip install django-seed
   - INSTALLED_APPS = [ 'django_seed', ]
   - python manage.py seed 앱이름 --number=10