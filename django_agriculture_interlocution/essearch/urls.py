from django.urls import path
from .views import EsAddDataView, EsSearch


urlpatterns = [
    path('adddata/', EsAddDataView.as_view(), name='add_data'),
    path('search/', EsSearch.as_view(), name='search'),
]