from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from movies.models import Movie, Genre, Crew, MovieCrew, Role, MovieComment


# class MovieSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     release_date = serializers.DateField()
#     avatar = serializers.ImageField(required=False)
#     view_count = serializers.IntegerField(read_only=True)
#     created_time = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         instance = Movie.objects.create(**validated_data)
#
#         return instance
#
#     def update(self, instance, validated_data):
#         pass


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('title',)


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class MovieCrewSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    crew = CrewSerializer()

    class Meta:
        model = MovieCrew
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    temp_field = serializers.BooleanField(default=True)
    is_released = serializers.SerializerMethodField()
    genres = GenreSerializer(many=True, read_only=True)
    movie_crew = MovieCrewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'avatar', 'view_count',
                  'created_time', 'temp_field', 'is_released', 'genres', 'movie_crew')
        read_only_fields = ('view_count', )
        extra_kwargs = {'release_date': {'write_only': True}, 'avatar': {'required': False}}

    def get_is_released(self, obj):
        if not obj.release_date:
            return None

        return timezone.now().date() >= obj.release_date

    def validate_title(self, attr):
        if 'ali' in attr:
            raise ValidationError('Title cannot contain ali')

        return attr.upper()

    def validate(self, attrs):
        release_date = attrs['release_date']
        avatar = attrs.get('avatar')

        date = timezone.datetime.strptime('2020-10-01', '%Y-%m-%d').date()
        if release_date > date and not avatar:
            raise ValidationError('This movie should have avatar')

        attrs['is_valid'] = False
        return attrs

    def create(self, validated_data):
        temp_field = validated_data.pop('temp_field')
        # genres = validated_data.pop('genres')
        instance = Movie.objects.create(**validated_data)

        # for genre in genres:
        #     genre, created = Genre.objects.get_or_create(title=genre['title'])
        #     instance.genres.add(genre)

        return instance

    def update(self, instance, validated_data):
        pass


class MovieCommentSerializer(serializers.ModelSerializer):
    # movie_data = MovieSerializer(read_only=True, source='movie')

    class Meta:
        model = MovieComment
        fields = ('id', 'parent', 'comment_body', 'movie')
        extra_kwargs = {'parent': {'allow_null': True, 'required': False}}

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(MovieCommentSerializer, self).create(validated_data)

    def to_representation(self, instance):
        res = super(MovieCommentSerializer, self).to_representation(instance)
        res['movie'] = MovieSerializer(instance.movie).data
        return res
