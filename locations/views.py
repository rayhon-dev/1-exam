from rest_framework import generics
from .serializers import LocationSerializer
from .pagination import LocationPagination
from .models import Location


class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = LocationPagination

class LocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
