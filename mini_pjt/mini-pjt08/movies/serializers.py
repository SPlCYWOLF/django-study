from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name',)


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title',)


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies',)


class ReviewListSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(
        source='movie.title',
        read_only=True,
    )

    class Meta:
        model = Review
        fields = '__all__'
        exlcude = ('content', 'rank',)


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorListSerializer(many=True, read_only=True,)
    reviews = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'release_date', 'poster_path', 'actors', 'reviews',)
        # fields = '__all__'
        # excludes = ('reviews',)


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(
        source='movie.title',
        read_only=True,
    )

    class Meta:
        model = Review
        fields = '__all__'