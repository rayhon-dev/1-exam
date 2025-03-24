from rest_framework import viewsets
from rest_framework import generics
from .serializers import WeatherDataSerializer, WeatherDataByLocationSerializer
from .pagination import WeatherDataPagination, WeatherDataByLocationPagination
from .models import WeatherData


class WeatherDataListCreateView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    pagination_class = WeatherDataPagination


class WeatherDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer


class  WeatherDataByLocationView(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataByLocationSerializer
    pagination_class = WeatherDataByLocationPagination

    def get_queryset(self):
       return super().get_queryset().filter(location__id=self.kwargs['pk'])


    # @action(detail=False, methods=['get'], url_path='analytics/temperature-avg')
    # def temperature_avg(self, request):
    #     avg_temp = WeatherData.objects.aggregate(average_temperature=Avg('temperature'))
    #     return Response(avg_temp)
    #
    # @action(detail=False, methods=['get'], url_path='analytics/precipitation-sum')
    # def precipitation_sum(self, request):
    #     total_precipitation = WeatherData.objects.aggregate(total_precipitation=Sum('precipitation'))
    #     return Response(total_precipitation)
    #
    # @action(detail=False, methods=['get'], url_path='analytics/wind-speed-max')
    # def wind_speed_max(self, request):
    #     max_wind_speed = WeatherData.objects.aggregate(max_wind_speed=Max('wind_speed'))
    #     return Response(max_wind_speed)
    #
    #
