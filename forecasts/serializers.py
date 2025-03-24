from rest_framework import serializers
from .models import Forecast

class ForecastLocation(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = [
            'id',
            'location',
            'forecast_date',
            'temperature_min',
            'temperature_max',
            'humidity',
            'precipitation_probability',
            'wind_speed',
            'wind_direction',
            'created_at'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['location'] = ForecastLocation(instance.location).data
        return data

class ForecastByLocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    forecast_date = serializers.DateField(read_only=True)
    temperature_min = serializers.FloatField(read_only=True)
    temperature_max = serializers.FloatField(read_only=True)
    humidity = serializers.FloatField(read_only=True)
    precipitation_probability = serializers.FloatField(read_only=True)
    wind_speed = serializers.FloatField(read_only=True)
    wind_direction = serializers.FloatField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

