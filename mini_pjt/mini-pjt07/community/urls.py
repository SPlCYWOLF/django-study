from . import views
from django.urls import path

app_name = 'community'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:review_pk>/like/', views.like, name='like'),
]
