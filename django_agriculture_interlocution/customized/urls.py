from django.urls import path
from .views import HarvestRequestView,IrrigationRequestView

urlpatterns = [
    path('harvesting/', HarvestRequestView.as_view(), name='harvest_request'),
    path('irrigation/', IrrigationRequestView.as_view(), name='irrigation_request'),
]