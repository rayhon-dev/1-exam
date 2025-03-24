from rest_framework import generics
from .serializers import ForecastSerializer, ForecastByLocationSerializer
from .pagination import ForecastPagination, ForecastByLocationPagination
from .models import Forecast


class ForecastListCreateView(generics.ListCreateAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    pagination_class = ForecastPagination


class ForecastRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer


class ForecastByLocationView(generics.ListAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastByLocationSerializer
    pagination_class = ForecastByLocationPagination

    def get_queryset(self):
       return super().get_queryset().filter(location__id=self.kwargs['pk'])
