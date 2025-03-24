from django.urls import path
from . import views


urlpatterns = [
    path('locations/', views.LocationListCreateView.as_view(), name='list-create'),
    path('locations/<int:pk>/', views.LocationRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete'),
]