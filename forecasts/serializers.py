from rest_framework import serializers
from .models import Forecast
from .validators import validate_forecast_date, validate_temperature_range
from locations.models import Location


class ForecastSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    forecast_date = serializers.DateField(validators=[validate_forecast_date])

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

    def validate(self, data):
        validate_temperature_range(data.get('temperature_min'), data.get('temperature_max'))
        return data
