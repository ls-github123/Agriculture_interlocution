from django.urls import path
from .views import HarvestRequestView

urlpatterns = [
    path('api/harvesting/', HarvestRequestView.as_view(), name='harvest_request'),
]