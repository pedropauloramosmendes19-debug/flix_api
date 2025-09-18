from django.db.models import Avg
from rest_framework import serializers
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = "__all__"


    def validate_release_date(self, value):
        if value.year < 1970:
            raise serializers.ValidationError('Ano de lançamento não pode ser antes de 1970')
        return value

    def validate_resume(self, value):
        if len(value) > 300:
            raise serializers.ValidationError('O resumo não pode ter mais do que 300 caracteres')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    cast = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date', 'resume', 'cast', 'rate']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('review'))['review__avg']
        if rate:
            return rate
        return None