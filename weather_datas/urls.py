from django.urls import path
from . import views


urlpatterns = [
    path('weather-data/', views.WeatherDataListCreateView.as_view(), name='list-create'),
    path('weather-data/<int:pk>/', views.WeatherDataRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete'),
    path('weather-data/location/<int:pk>/', views.WeatherDataByLocationView.as_view(), name='weather-data-by-location')
]