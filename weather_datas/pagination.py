from rest_framework.pagination import PageNumberPagination


class WeatherDataPagination(PageNumberPagination):
    page_size = 10

class WeatherDataByLocationPagination(PageNumberPagination):
    page_size = 5