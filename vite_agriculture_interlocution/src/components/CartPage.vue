<template>
    <div>
      <h1>购物车</h1>
      <div v-if="cart.cart_items.length > 0">
        <div v-for="item in cart.cart_items" :key="item.id" class="cart-item">
          <p>{{ item.product.name }} - {{ item.quantity }} x {{ item.product.price }}元
            <button @click="removeFromCart(item.id)">删除</button>
          </p>
        </div>
        <p>总价: {{ cart.total_price }}元</p>
        <button @click="checkout">生成订单</button>
      </div>
      <p v-else>购物车为空</p>
      <button @click="goToOrders">查看订单列表</button>  <!-- 新增跳转订单列表按钮 -->
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
      // 获取购物车内容
      async fetchCart() {
        try {
          const response = await axios.get('http://localhost:8000/api/cart/');
          this.cart = response.data;
        } catch (error) {
          console.error('Failed to fetch cart:', error);
        }
      },
  
      // 删除购物车中的商品
      async removeFromCart(itemId) {
        try {
          await axios.delete(`http://localhost:8000/api/cart/items/${itemId}/`);
          this.cart.cart_items = this.cart.cart_items.filter(item => item.id !== itemId);
          this.cart.total_price = this.cart.cart_items.reduce((total, item) => total + parseFloat(item.total_price), 0);
        } catch (error) {
          console.error('Failed to remove item:', error);
        }
      },
  
      // 结算并创建订单
      async checkout() {
        try {
          const response = await axios.post('http://localhost:8000/api/cart/checkout/');
          alert('订单已创建，订单ID：' + response.data.order_id);
          this.cart = {
            cart_items: [],
            total_price: 0
          };
        } catch (error) {
          console.error('Failed to create order:', error);
        }
      },
  
      // 跳转到订单列表
      goToOrders() {
        this.$router.push({ name: 'OrderListPage' });
      }
    }
  };
  </script>
  