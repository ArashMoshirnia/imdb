from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets

from movies.models import Movie, MovieComment
from movies.api.serializers import MovieSerializer, MovieCommentSerializer
from movies.permissions import MovieCommentPermission
from movies.throttles import MoviesListThrottle


@api_view(['GET', 'POST'])
def movies_list_api(request):
    if request.method == 'GET':
        movies = Movie.valid_objects.prefetch_related('genres', 'crew')
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
    serializer_class = MovieSerializer
    # parser_classes = [JSONParser, MultiPartParser]
    # renderer_classes = [JSONRenderer]

    # def get_queryset(self):
    #     a_month_ago = timezone.now().date() - timezone.timedelta(days=30)
    #     queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
    #     if self.request.method == 'GET':
    #         queryset = queryset.filter(release_date__gte=a_month_ago)
    #
    #     return queryset


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
    serializer_class = MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'movies'
    queryset = Movie.valid_objects.prefetch_related('genres', 'crew')
    serializer_class = MovieSerializer

    def get_throttles(self):
        if self.action == 'list':
            return [MoviesListThrottle()]

        return [ScopedRateThrottle()]

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticatedOrReadOnly()]

        elif self.action == 'rate':
            return [IsAuthenticated()]

        return [AllowAny()]

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        print(request.user)
        return super(MovieViewSet, self).list(request, *args, **kwargs)

    @action(methods=['POST'], detail=False, url_path='movie_rate')
    def rate(self, request, *args, **kwargs):
        return Response({'result': f'rate submitted for movie'})


class MovieCommentView(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (MovieCommentPermission, )
    queryset = MovieComment.objects.all()
    serializer_class = MovieCommentSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
