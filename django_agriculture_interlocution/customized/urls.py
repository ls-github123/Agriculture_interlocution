from django.urls import path,include
from .views import HarvestRequestView,IrrigationRequestView,CropViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'crops', CropViewSet)
urlpatterns = [
    
    path('harvesting/', HarvestRequestView.as_view(), name='harvest_request'),
    path('irrigation/', IrrigationRequestView.as_view(), name='irrigation_request'),
     path('', include(router.urls)),
    

]