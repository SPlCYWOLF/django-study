from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.actor_list),                      # 전체 배우 목록
    path('actors/<int:actor_pk>', views.actor_detail),      # 단일 배우 정보(출연 영화 포함)

    path('movies/', views.movie_list),                      # 전체 영화 목록
    path('movies/<int:movie_pk>/', views.movie_detail),     # 단일 영화 정보(출연 배우, 리뷰 데이터 목록 포함)

    path('reviews/', views.review_list),                    # 전체 리뷰 목록 조회
    path('movies/<int:movie_pk>/reviews/', views.review_create),        # 리뷰 생성
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail_or_update_or_delete),    # 단일 리뷰 정보(영화 정보 포함)/수정/삭제
]