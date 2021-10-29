from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer


# 전체 배우 목록 조회
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


# 단일 배우 정보 조회
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


# 전체 영화 목록 조회
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 단일 영화 정보 조회
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 전체 리뷰 목록
@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


# 리뷰 생성
@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 단일 리뷰 정보 조회/수정/삭제
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review_title = review.title     # 리뷰 제목을 남겨주고 싶었어

    # 단일 리뷰 조회
    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


    # 단일 리뷰 수정
    elif request.method == "PUT":
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    # 단일 리뷰 삭제
    else:
        review.delete()
        return Response({ review_title }, status=status.HTTP_204_NO_CONTENT)