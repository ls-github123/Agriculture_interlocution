from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import ProductSerializer, CartSerializer

# 获取商品列表
class ProductListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = agr_Product.objects.all()
        data = [
            {
                "id": product.id,
                "name": product.name,
                "price": str(product.price)
            } for product in products
        ]
        return Response(data)
    





# 获取购物车信息
class CartView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            # 获取购物车 (假设通过用户标识来获取购物车)
            cart, created = agr_Cart.objects.get_or_create(user="guest")

            # 更新购物车总价
            cart.update_total_price()

            # 获取购物车中的商品项
            cart_items = cart.cart_items.all()  # 使用 'cart_items' 反向关系
            cart_items_data = [
                {
                    "id": item.id,
                    "product": {
                        "id": item.product.id,
                        "name": item.product.name,
                        "price": str(item.product.price)
                    },
                    "quantity": item.quantity,
                    "total_price": str(item.total_price())
                }
                for item in cart_items
            ]

            return Response({
                "cart_id": cart.id,
                "total_price": str(cart.total_price),
                "cart_items": cart_items_data
            })
        except Exception as e:
            return Response({'error': str(e)}, status=500)




    # 向购物车添加商品
class AddToCartView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            # 获取商品ID和数量
            product_id = request.data.get('product_id')
            quantity = request.data.get('quantity', 1)

            if not product_id:
                return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)

            # 查找商品
            product = agr_Product.objects.get(id=product_id)
            cart, created = agr_Cart.objects.get_or_create(user="guest")  # 假设购物车由guest用户管理

            # 判断商品是否已在购物车中
            cart_item, created = agr_CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity  # 如果已存在，增加商品数量
            cart_item.save()

            # 更新购物车总价
            cart.update_total_price()

            return Response({'message': '商品已加入购物车'}, status=status.HTTP_201_CREATED)

        except agr_Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class RemoveFromCartView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, item_id):
        try:
            cart_item = agr_CartItem.objects.get(id=item_id)
            cart_item.delete()  # 删除购物车项

            # 更新购物车总价
            cart_item.cart.update_total_price()

            return Response({'message': '商品已从购物车中删除'}, status=status.HTTP_200_OK)

        except agr_CartItem.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)