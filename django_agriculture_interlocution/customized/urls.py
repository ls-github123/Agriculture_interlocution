from django.urls import path
from .views import HarvestRequestView,IrrigationRequestView

urlpatterns = [
    path('api/harvesting/', HarvestRequestView.as_view(), name='harvest_request'),
    path('api/irrigation/', IrrigationRequestView.as_view(), name='irrigation_request'),
]