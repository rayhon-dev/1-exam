from django.urls import path
from . import views


urlpatterns = [
    path('analytics/temperature-avg/', views.average_temperature_view, name='temperature-avg'),
    path('analytics/precipitation-sum/', views.total_precipitation_view, name='total-precipitation'),
    path('analytics/wind-speed-max/', views.max_wind_speed_view, name='max-wind-speed')
]