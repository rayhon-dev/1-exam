from rest_framework.pagination import PageNumberPagination

class LocationPagination(PageNumberPagination):
    page_size = 10
