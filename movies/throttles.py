from rest_framework import throttling


class MoviesListThrottle(throttling.AnonRateThrottle):
    rate = '6/min'
