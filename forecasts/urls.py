from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ForecastViewSet

router = DefaultRouter()
router.register(r'forecasts', ForecastViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

