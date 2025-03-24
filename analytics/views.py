from django.db.models import Avg, Sum, Max
from rest_framework.response import Response
from rest_framework.decorators import api_view
from weather_datas.models import WeatherData




@api_view(['GET'])
def average_temperature_view(request):
    avg_value = WeatherData.objects.aggregate(average_temperature=Avg('temperature'))
    return Response(avg_value)


@api_view(['GET'])
def total_precipitation_view(request):
    total_precipitation = WeatherData.objects.aggregate(total_precipitation=Sum('precipitation'))
    return Response(total_precipitation)


@api_view(['GET'])
def max_wind_speed_view(request):
    max_wind_speed = WeatherData.objects.aggregate(max_wind_speed=Max('wind_speed'))
    return Response(max_wind_speed)
