from django.urls import path
from . import views


urlpatterns = [
    path('forecasts/', views.ForecastListCreateView.as_view(), name='list-create'),
    path('forecasts/<int:pk>/', views.ForecastRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete'),
    path('forecasts/location/<int:pk>/', views.ForecastByLocationView.as_view(), name='forecast-by-location')
]