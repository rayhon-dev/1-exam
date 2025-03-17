from rest_framework import viewsets
from .serializers import WeatherDataSerializer
from .models import WeatherData
from rest_framework.decorators import action
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