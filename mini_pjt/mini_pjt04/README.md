# Simple forum

by Tae Hun KIM, 

partnered with Jang Hoon O

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"/>  <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">



1. [Build-process](#build-process)
2. [Acquired knowledge](#acquired knowledge)
3. [Challenge & Solution](#challenge & solution)

<hr>





## Build-process (paired programming)

<hr>

1. utilized django to set up the basic CRUD structure.

2. created the 'parent' template folder to remove repetitive html elements.

   ```python
   # urls.py (project directory)
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('movies/', include('movies.urls'))
   ]
   ```

   ```html
   {% comment %} base.html {% endcomment %}
   <body>
     <nav class="navbar navbar-expand-lg navbar-light bg-light">
     <div class="container-fluid">
       <a class="navbar-brand" href="#">Navbar</a>
       <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="collapse navbar-collapse" id="navbarNav">
         <ul class="navbar-nav">
           <li class="nav-item">
             <a class="nav-link active" aria-current="page" href=" {% url 'movies:index' %}">영화목록</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href=" {% url 'movies:new' %}">게시글 작성</a>
           </li>
         </ul>
       </div>
     </div>
   </nav>
   
     {% block content %}{% endblock %}
     
     {% comment %} bootstrap {% endcomment %}
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
   </body>
   ```

3. constructed the overall structure of the project through listing all the necessary url patterns.

   ```python
   app_name = 'movies'
   
   urlpatterns = [
       path('', views.index, name='index'),
       path('new/', views.new, name='new'),
       path('create/', views.create, name='create'),
       path('<int:movie_pk>/', views.detail, name='detail'),
       path('<int:movie_pk>/edit/', views.edit, name='edit'),
       path('<int:movie_pk>/update/', views.update, name='update'),
       path('<int:movie_pk>/delete/', views.delete, name='delete'),
   ]
   ```

4. defined the name of Model class to create a blueprint for the Table.

   ```python
   class Movie(models.Model):
       title = models.CharField(max_length=100)
       overview = models.TextField()
       poster_path = models.CharField(max_length=500)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

5. created functions at `views.py` to forward requests from the client to adequate templates.

   ```python
   # an example function for sending a request to create new post,
   # and showing the new post to the client
   def create(request):
       title = request.POST.get('title')
       overview = request.POST.get('overview')
       poster_path = request.POST.get('poster_path')
       movie = Movie(title=title, overview=overview, poster_path=poster_path)
       movie.save()
       return redirect('movies:detail', movie.pk)
   ```

6. created html templates that will be given(shown) to the clients as a response.

   ```html
   {% comment %} index.html {% endcomment %}
   {% extends 'base.html' %}
   {% block content %}
     <h1>INDEX</h1>
     <a href=" {% url 'movies:new' %}">게시글 작성</a>
     {% for movie in movies %}
       <h2>제목: {{ movie.title }}</h2>
       <p>내용: {{ movie.overview }}</p>
       <a href=" {% url 'movies:detail' movie.pk %}">자세히</a>
     {% endfor %}
   {% endblock %}
   ```

7. lastly, added minor features, such as buttons, csrf token, and design improvements to finalize the project.







## Acquired knowledge

<hr>

#### Using an ORM (object relational mapping)

- utilized python (OOP method) to communicate between Django and SQLite, which are not compatible in programming language.

- python send request to SQLite using DB API, and receives responses through QuerySet API.

- helped saving input data from the client on the Database.

  ```python
  def create(request):
      title = request.POST.get('title')
      overview = request.POST.get('overview')
      poster_path = request.POST.get('poster_path')
      movie = Movie(title=title, overview=overview, poster_path=poster_path)
      movie.save()
      return redirect('movies:detail', movie.pk)
  ```



#### Django web framework basics

- django is one of the most productive webframework with a promising quality.

- it provides superior admin-page for Creating, Reading, Updating, and Deleting tables stored in the DB.

  ```python
  from django.contrib import admin
  from .models import Movie
  # Register your models here.
  admin.site.register(Movie)
  ```

- django contains number of convenient modules, significantly reducing the building-process.

  Some of the examples are, simplifying the process of migration and communications between Model, View, and Templates.

  ```python
  from django.shortcuts import render, redirect
  from django.urls import path, include
  ```

- django provides a simple minimun security solution called, CSRF token.

  - it is useful to blockade cross site request forgery

  ```html
  <form action=" {% url 'movies:create' %} " method='POST'>
    {% csrf_token %}
    <label for="title">title: </label>
    <input type="text" name="title">
  ```

  #### - CRUD

  - it is an abbreviation of create, read, update, and delete.
  - most SW maintains such structure.
  - Django provides a solid frame to quickly construct the CRUD.







## Challenge & Solution

<hr>

1. visualizing the overall structure of Model Template View of others.

One's capability of visualizing the overall structure of the project determines the individual's productivity.

Nevertheless, most web-developments are done in team.

Understanding partner's overall picture of the project, and the procedure in his or her mind is essential for increasing the team's productivity.

This project was completed in paired-programming, and it was a good opportunity to train such challenging task.

There was nothing special. I simply communicated --constantly.

When I was a 'driver'(coder), I did not care if what I'm doing were obvious tasks, I explained the reason for every single moves I made. And when I got stuck, or did not understand the 'navigator' order, I asked until I understood his intention.

When I was a 'navigator', I explained every single orders I made, and asked the 'driver' to interrupt if the explanation isn't satisfying.



#### Takeaway

Indeed, trying to verbalize every single thoughts was a tough process. But through this project, I was once again reminded with the importance of communication in web-development.