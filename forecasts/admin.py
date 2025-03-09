from django.contrib import admin
from .models import Forecast

@admin.register(Forecast)
class ForecastDateAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'forecast_date', 'temperature_min', 'temperature_min', 'humidity', 'precipitation_probability', 'wind_speed', 'wind_direction']
    search_fields = ['location']
