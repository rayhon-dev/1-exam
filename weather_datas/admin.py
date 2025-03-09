from django.contrib import admin
from .models import WeatherDate

@admin.register(WeatherDate)
class WeatherDateAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'temperature', 'humidity', 'pressure', 'wind_speed', 'wind_direction', 'precipitation']
    search_fields = ['location']
