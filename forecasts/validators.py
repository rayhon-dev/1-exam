from rest_framework import serializers
from datetime import date

def validate_forecast_date(value):
    if value < date.today():
        raise serializers.ValidationError("Forecast date cannot be in the past.")
    return value

def validate_temperature_range(min_temp, max_temp):
    if min_temp > max_temp:
        raise serializers.ValidationError("Minimum temperature cannot be greater than maximum temperature.")
