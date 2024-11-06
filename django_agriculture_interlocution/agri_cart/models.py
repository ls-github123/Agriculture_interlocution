# Create your models here.
from django.db import models

# 商品模型
class agr_Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='商品名')
    description = models.TextField(verbose_name='商品描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    stock = models.IntegerField(verbose_name='库存')

    def __str__(self):
        return self.name

# 购物车模型
class agr_Cart(models.Model):
    user = models.CharField(max_length=100, default="guest", verbose_name="用户标识")  # 假设没有认证，使用用户名或 guest 区分
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='总价')

    def __str__(self):
        return f"购物车 {self.user}"

    def update_total_price(self):
        total = sum(item.total_price() for item in self.cart_items.all())  # 通过反向关系获取购物车项
        self.total_price = total
        self.save()

# 购物车项模型，表示购物车中的每个商品
class agr_CartItem(models.Model):
    cart = models.ForeignKey(agr_Cart, on_delete=models.CASCADE, related_name='cart_items', verbose_name='购物车')
    product = models.ForeignKey(agr_Product, on_delete=models.CASCADE, verbose_name='商品')
    quantity = models.PositiveIntegerField(default=1, verbose_name='数量')

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"