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
        """
        更新购物车的总价，每次购物车内商品变动时调用此方法。
        计算购物车所有商品项的价格并保存到total_price字段。
        """
        total = sum(item.total_price() for item in self.cart_items.all())  # 通过反向关系获取购物车项
        self.total_price = total
        self.save()

# 购物车项模型，表示购物车中的每个商品
class agr_CartItem(models.Model):
    cart = models.ForeignKey(agr_Cart, on_delete=models.CASCADE, related_name='cart_items', verbose_name='购物车')
    product = models.ForeignKey(agr_Product, on_delete=models.CASCADE, verbose_name='商品')
    quantity = models.PositiveIntegerField(default=1, verbose_name='数量')

    def total_price(self):
        """ 计算单个购物车项的总价 """
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
# 订单模型
class agr_Order(models.Model):
    user = models.CharField(max_length=100, default='guest')  # 用户，guest代表未登录用户
    cart = models.ForeignKey(agr_Cart, on_delete=models.CASCADE)  # 购物车
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # 订单总价
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return f"订单 {self.id} - {self.user}"

    def update_total_price(self):
        """ 更新订单总价为购物车的总价 """
        self.total_price = self.cart.total_price
        self.save()
