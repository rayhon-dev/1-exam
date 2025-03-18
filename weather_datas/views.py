from rest_framework import viewsets
from .serializers import WeatherDataSerializer
from .models import WeatherData
from rest_framework.decorators import action
from django.db.models import Avg, Sum, Max
from rest_framework.response import Response


class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    @action(detail=False, methods=['get'],  url_path='location/(?P<location_id>\d+)')
    def location(self, request, location_id=None):
        # /api/weather-data/location/{pk}/
        weather_data = WeatherData.objects.filter(location_id=location_id)
        serializer = self.get_serializer(weather_data, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='analytics/temperature-avg')
    def temperature_avg(self, request):
        avg_temp = WeatherData.objects.aggregate(average_temperature=Avg('temperature'))
        return Response(avg_temp)

    @action(detail=False, methods=['get'], url_path='analytics/precipitation-sum')
    def precipitation_sum(self, request):
        total_precipitation = WeatherData.objects.aggregate(total_precipitation=Sum('precipitation'))
        return Response(total_precipitation)

    @action(detail=False, methods=['get'], url_path='analytics/wind-speed-max')
    def wind_speed_max(self, request):
        max_wind_speed = WeatherData.objects.aggregate(max_wind_speed=Max('wind_speed'))
        return Response(max_wind_speed)


