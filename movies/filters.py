import django_filters

from movies.models import Movie


class MovieFilterSet(django_filters.FilterSet):
    min_release_date = django_filters.DateFilter(field_name='release_date', lookup_expr='gte') # release_date__gte
    max_release_date = django_filters.DateFilter(field_name='release_date', lookup_expr='lt') # release_date__lt
    genre = django_filters.CharFilter(field_name='genres__title')

    class Meta:
        model = Movie
        fields = ('title', )
