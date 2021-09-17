# Simple forum 2

by Tae Hun KIM, 

partnered with Dong Wan Yu

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"/>  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">  <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">



1. [Build-process](#build-process)
2. [Acquired knowledge](#acquired knowledge)
3. [Challenges & Solutions](#challenges & solutions)
4. [Takeaway](#takeaway)

<hr>
<br>
<br>

<br>


## :handshake:  Build-process (페어 프로그래밍)

<hr>

1. 이번 설명은, 새로운 구현 요소들 위주로 이루어졌습니다.

   이전 프로젝트와 유사하게, 장고 프레임워크를 이용하여 명세서에 적힌 대로 기본적인 CRUD 를 구현하기 위한 틀을 잡는것부터 시작했습니다.

   model, view, templates, 그리고 프로젝트에서는 처음 사용해보는 static file 과 media file 의 경로들도 지정해 주었습니다. 

   ```python
   # settings.py
   ...
   STATIC_URL = '/static/'
   STATIC_ROOT = BASE_DIR / 'static_files'
   STATICFILES_DIRS = [BASE_DIR / 'static']
   
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

   특히, 업로드 된 파일을 DB에 저장 할 수 있도록 아래와 같이 파일의 `url` 을 읽어와야 했습니다.

   ```python
   # urls.py (앱 폴더)
   from django.conf import settings
   from django.conf.urls.static import static
   
   app_name = 'movies'
   urlpatterns = [
   	...
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

   <br>

2. 다음으로, `Movie`의 필드값들을 정의하는데, 업로드 이미지 파일이 저장되는 위치를 지정했습니다.

   ```python
   class Movie(models.Model):
       title = models.CharField(max_length=100)
       overview = models.TextField()
       image = models.ImageField(blank=True, upload_to='images/')
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

   <br>

3. 업로드된 이미지에 대한 정보를 담은 `POST `요청을 view.py 에서 잘 처리 할 수 있게 `form` 인스턴스 생성 단계에서 `files`키워드 인자를 추가로 넣어주었습니다.

   ```python
   # views.py
   def create(request):
       if request.method == 'POST':
           form = MovieForm(data=request.POST, files=request.FILES)
           ...
   ```

   <br>

4. 이전 프로젝트에서는 따로 작성 되었던 `create.html` 과 `update.html`을 조건문을 활용하여 하나로 합친 `form.html` 을 작성하였습니다.

   조건문은, 타고 들어오는 `url` 의 `name` 에 의해 결정됩니다 (name=create 혹은 name=update)

   ```html
   {% comment %} form.html {% endcomment %}
   {% extends 'base.html' %}
   {% load static %}
   
   {% block content %}
     {% if request.resolver_match.url_name == "create" %}
       <h2>영화 작성</h2>
       <form class="d-inline" action="{% url 'movies:create' %}" method="POST" enctype="multipart/form-data">
         {% csrf_token %}
         {{ form.as_p }}
         <button class="btn btn-primary">작성</button>
       </form>
       <a href="{% url 'movies:index' %}"><button class="btn btn-dark">취소</button></a>
       
       {% else %}
         <h2>영화 수정</h2>
         <form class="d-inline" action="{% url 'movies:update' movie.pk %}" method="POST" enctype="multipart/form-data">
           {% csrf_token %}
           {{ form.as_p }}
           <button class="btn btn-primary">작성</button>
       </form>
       <a href="{% url 'movies:detail' movie.pk %}"><button class="btn btn-dark">취소</button></a>
     {% endif %}
   {% endblock  %}
   ```

   <br>

5. 마지막으로, bootstrap을 활용하여 기본적인 템플릿들의 외형을 다듬었습니다.

<hr>
<br>
<br>

<br>


## :memo:  Acquired knowledge 

<hr>

#### Bootstrap_pagination

- 밋밋한 기본 pagination 을 간단한 코드로 장식해주는 bootstrap의 코드입니다.

  ```python
  # views.py
  from .models import Movie
  from django.core.paginator import Paginator
  
  def index(request):
      movies = Movie.objects.order_by('-pk')
      paginator = Paginator(movies, 4)
  
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
      context = {
          'page_obj': page_obj,
      }
      return render(request, 'movies/index.html', context)
  ```

- ```html
  {% comment %} index.html {% endcomment %}
  {% load bootstrap5 %}
  ...
    <div class="d-flex justify-content-center mt-4">
      {% bootstrap_pagination page_obj %}
    </div>
  ```

<br>

#### include 탬플릿 태그

- 하나의 html 파일의 내용들이 너무 많아져 번잡해 졌을때 사용하면 좋은 기능입니다.

- 이번 프로젝트에서는, `navbar` 의 코드를 `base.html`에 작성하는데 include 탬플릿 태그를 사용하여 가독성을 높였습니다.

- 참고로 `navbar` 의 파일명 앞의  `_` 는 의미론적인 컨벤션입니다.

  ```html
  {% comment %} _navbar.html {% endcomment %}
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">pjt05</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'movies:index' %}">영화 목록</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'movies:create' %}">영화 작성</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  ```

- ```html
  {% comment %} base.html {% endcomment %}
  ...
  <body>
    <div class="container">
      {% include "_navbar.html" %}
      {% block content %}
      {% endblock %}
    </div>
  ```

<hr>
<br>
<br>

<br>

## :fire:  Challenges & Solutions 

#### 1. Problem: 이미지 파일이 업로드 안 된 경우


   - 상세 페이지의 템플릿은, 모든 필드 값들이 충족된 상태를 전재로 만들어졌습니다. Title 과 Overview 필드는 빈 값을 허용하지 않도록 `is_valid()` 함수를 활용했습니다.

     하지만, 이미지 같은 경우는 조금 다르다 생각했습니다. Rotten Tomatoes, IMDB와 같은 영화 정보/리뷰 사이트를 보면, 내용 혹은 제목만 빠진 영화 정보는 없지만, 이미지만 없는 영화 정보는 많았습니다. 그레서 이미지 파일 같은 경우는, 업로드가 안되면 준비해 놓은 `no_image.png`를 보여주도록 했습니다.
     
     
     
     #### Solution: `views.py` 상에서 조건문 걸어주기
     
   - 업로드 된 파일의 url 값이 저장되어 있는 필드값: `image` , 가 공백일 경우, `static/movies/images/no_image.png` 에 위치한 이미지 파일의 url을 해당 `movie` 인스턴스에 저장, 해당 인스턴스의 필드값들은 details 페이지에서 사용자에게 보여집니다.

   - ```python
     @require_http_methods(['GET', 'POST'])
     def update(request, pk):
         ...
                 if not movie.image:
                     movie.image = 'images/no_image.png'
                 movie.save()
                 return redirect('movies:detail', movie.pk)
         ...
     ```

<br>

#### 2. Problem: 영화 정보 삭제 시, 이미지 파일은 삭제 되지 않는 현상

- 상세 페이지에서 영화 정보 삭제를 시켜도, `movies/images/` 폴더 안에 있는 삭제 대상인 이	미지 파일은 사라지지 않았습니다.

  

  #### Solution: `pip install django-cleanup`

- 장고 내장 3rd party library 인 django-cleanup 을 이용해 영화 정보 삭제 요청이 전송되면, 해당 record 값의 이미지 필드에 기록된 경로의 이미지 파일도 삭제 되도록 하였습니다.

- 추가 코드 없이 간편했습니다.

- ```python
  # settings.py
  INSTALLED_APPS = [
  	...,
  	'django_cleanup'
  ]
  ```

<hr>
<br>
<br>

<br>


## :shopping_cart:  Takeaway

<hr>

이전 프로젝트 (pjt04) 와는 다르게 온전히 네이게이터 역할로 프로젝트를 수행했습니다.

제 파트너이자 드라이버 역할을 맡아주셨던 동완님께서 너무 잘 해주셔서, 결과물로써는 정말 만족스러운 프로젝트이지 않았나 생각합니다. 하지만 아쉬운 부분이 있었다면, 이 프로젝트를 마주하는데에 대한 서로간에 타협이 부족했고, 결과적으로 생산성의 저하로 이어지지 않았나 생각됩니다. 

저는, 기능적 UX개선을 항상 의식했지만, 드라이버 분께서는 시각적 UX를 확실하게 개선하려 하셨습니다. 이러한 프로젝트를 대하는 자세의 차이는, 프로젝트 후반에 접어들 수록 생산성에 영향을 많이 미쳤습니다. 왜냐하면, 한쪽만 잘 알고, 나머지 한쪽은 잘 모르는 부분에 집중하게 되면, 아무래도 1인 플레이가 되어버리기 때문입니다.

다음 페어 프로그래밍을 수행하게 된다면, 프로젝트 후반부에서의 생산성을 낮추지 않기 위해, 처음부터 파트너와 프로젝트의 목표에 대한 방향성을 수립해보는 것도 유익한 경험이 되지 않을까 생각했습니다.