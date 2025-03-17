from rest_framework import serializers
from .models import WeatherData
from locations.serializers import LocationShortSerializer
from .validators import validate_temperature, validate_humidity


class WeatherDataSerializer(serializers.ModelSerializer):
    location = LocationShortSerializer(read_only=True)
    temperature = serializers.FloatField(validators=[validate_temperature])
    humidity = serializers.FloatField(validators=[validate_humidity])

    class Meta:
        model = WeatherData
        fields = [
            'id',
            'location',
            'temperature',
            'humidity',
            'pressure',
            'wind_speed',
            'wind_direction',
            'precipitation',
            'recorded_at'
        ]