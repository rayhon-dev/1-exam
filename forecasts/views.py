from rest_framework import viewsets
from .models import Forecast
from .serializers import ForecastSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    @action(detail=False, methods=['get'], url_path='location/(?P<location_id>\d+)')
    def location(self, request, location_id=None):
        # /api/weather-data/location/{pk}/
        forecast = Forecast.objects.filter(location_id=location_id)
        serializer = self.get_serializer(forecast, many=True)
        return Response(serializer.data)

