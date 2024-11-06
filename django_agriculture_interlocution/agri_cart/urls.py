from django.urls import path
from .views import ProductListView, CartView,RemoveFromCartView,AddToCartView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartView.as_view(), name='cart-view'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/items/<int:item_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]