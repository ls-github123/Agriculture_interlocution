<template>
  <div class="cart-page">
    <!-- 返回上一页按钮 -->
    <button class="back-btn" @click="goBack">← 返回</button>

    <h1 class="title">购物车</h1>
    
    <div v-if="cart.cart_items.length > 0" class="cart-items-container">
      <div v-for="item in cart.cart_items" :key="item.id" class="cart-item">
        <div class="item-info">
          <p><strong>{{ item.product.name }}</strong> - {{ item.product.price }}元</p>
          <!-- 数量选择 -->
          <input type="number" v-model.number="item.quantity" min="1" class="quantity-input" />
        </div>
        <div class="item-actions">
          <!-- 更新数量按钮 -->
          <button class="update-btn" @click="updateQuantity(item.id, item.quantity)">更新</button>
          <!-- 删除按钮 -->
          <button class="remove-btn" @click="removeFromCart(item.id)">删除</button>
        </div>
      </div>
      <p class="total-price">总价: {{ cart.total_price }}元</p>
      <button class="checkout-btn" @click="checkout">生成订单</button>
    </div>
    
    <p v-else class="empty-cart">购物车为空</p>

    <button class="orders-btn" @click="goToOrders">查看订单列表</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cart: {
        cart_items: [],
        total_price: 0
      }
    };
  },
  created() {
    this.fetchCart();
  },
  methods: {
    async fetchCart() {
      try {
        const response = await axios.get('http://localhost:8000/agri_cart/cart/');
        this.cart = response.data;
      } catch (error) {
        console.error('Failed to fetch cart:', error);
      }
    },

    async updateQuantity(itemId, quantity) {
  try {
    await axios.patch(`http://localhost:8000/agri_cart/cart/items/${itemId}/`, {
      quantity: quantity
    });
    await this.fetchCart(); // 重新获取购物车数据，确保总价更新
  } catch (error) {
    console.error('Failed to update item quantity:', error);
  }
},

    async removeFromCart(itemId) {
      try {
        await axios.delete(`http://localhost:8000/agri_cart/cart/items/${itemId}/`);
        this.fetchCart();
      } catch (error) {
        console.error('Failed to remove item:', error);
      }
    },

    async checkout() {
      try {
        const response = await axios.post('http://localhost:8000/agri_cart/cart/checkout/');
        alert('订单已创建，订单ID：' + response.data.order_id);
        this.cart = {
          cart_items: [],
          total_price: 0
        };
      } catch (error) {
        console.error('Failed to create order:', error);
      }
    },

    goToOrders() {
      this.$router.push({ name: 'OrderListPage' });
    },

    goBack() {
      window.history.back();
    }
  }
};
</script>

<style scoped>
.cart-page {
  font-family: 'Arial', sans-serif;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  background-color: #f9fafb;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.back-btn {
  position: absolute;
  top: 20px;
  left: 20px;
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  font-size: 1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.back-btn:hover {
  background-color: #0056b3;
}

.title {
  font-size: 2.5em;
  font-weight: bold;
  text-align: center;
  color: #333;
  margin-top: 60px;
  margin-bottom: 30px;
}

.cart-items-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  padding: 15px 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.cart-item:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}

.item-info p {
  font-size: 1.2em;
  margin: 0;
  color: #444;
}

.item-info strong {
  color: #333;
}

.quantity-input {
  width: 60px;
  padding: 5px;
  font-size: 1em;
  text-align: center;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 10px;
}

.item-actions {
  display: flex;
  gap: 10px;
}

.update-btn {
  background-color: #ffc107;
  color: white;
  border: none;
  padding: 8px 15px;
  font-size: 1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.update-btn:hover {
  background-color: #e0a800;
}

.remove-btn {
  background-color: #dc3545;
  color: white;
  border: none;
  padding: 8px 15px;
  font-size: 1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.remove-btn:hover {
  background-color: #c82333;
}

.total-price {
  font-size: 1.5em;
  font-weight: bold;
  margin-top: 20px;
  text-align: right;
  color: #333;
}

.checkout-btn {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 15px 30px;
  font-size: 1.2em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 30px;
  display: block;
  margin-left: auto;
}

.checkout-btn:hover {
  background-color: #218838;
}

.empty-cart {
  text-align: center;
  font-size: 1.5em;
  color: #888;
}

.orders-btn {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 12px 25px;
  font-size: 1.1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 40px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.orders-btn:hover {
  background-color: #0056b3;
}
</style>
