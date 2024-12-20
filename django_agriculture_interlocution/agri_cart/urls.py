from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartView.as_view(), name='cart-view'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/items/<int:item_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/checkout/', CheckoutView.as_view(), name='create_order'),  # 结算/生成订单
    
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:id>/', OrderDetailView.as_view(), name='order-detail'),


    # 创建支付链接
    path('alipay/<int:order_id>/', AlipayPaymentView.as_view(), name='alipay_payment'),
    
    # 支付回调通知
    path('alipay/notify/', AlipayNotifyView.as_view(), name='alipay_notify'),

]