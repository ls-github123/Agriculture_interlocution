<template>
    <div class="cart-page">
      <!-- 返回上一页按钮 -->
      <button class="back-btn" @click="goBack">← 返回</button>
  
      <h1 class="title">购物车</h1>
      
      <div v-if="cart.cart_items.length > 0" class="cart-items-container">
        <div v-for="item in cart.cart_items" :key="item.id" class="cart-item">
          <div class="item-info">
            <p><strong>{{ item.product.name }}</strong> - {{ item.quantity }} x {{ item.product.price }}元</p>
          </div>
          <button class="remove-btn" @click="removeFromCart(item.id)">删除</button>
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
      },
  
      // 返回上一页
      goBack() {
        window.history.back();
      }
    }
  };
  </script>
  
  <style scoped>
  /* 整体页面样式 */
  .cart-page {
    font-family: 'Arial', sans-serif;
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
  }
  
  /* 返回按钮样式 */
  .back-btn {
    position: absolute;
    top: 20px;
    left: 20px;
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    font-size: 1.2em;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .back-btn:hover {
    background-color: #0056b3;
  }
  
  /* 标题样式 */
  .title {
    font-size: 2.5em;
    font-weight: bold;
    text-align: center;
    color: #333;
    margin-top: 60px;
    margin-bottom: 30px;
  }
  
  /* 购物车项容器 */
  .cart-items-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  /* 单个购物车商品项 */
  .cart-item {
    display: flex;
    justify-content: space-between;
    background-color: #fff;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .cart-item:hover {
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  }
  
  /* 商品信息 */
  .item-info p {
    font-size: 1.2em;
    margin: 5px 0;
  }
  
  .item-info strong {
    color: #333;
  }
  
  /* 删除按钮 */
  .remove-btn {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 1em;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .remove-btn:hover {
    background-color: #c82333;
  }
  
  /* 总价显示 */
  .total-price {
    font-size: 1.5em;
    font-weight: bold;
    margin-top: 20px;
  }
  
  /* 结算按钮 */
  .checkout-btn {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 12px 25px;
    font-size: 1.2em;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .checkout-btn:hover {
    background-color: #218838;
  }
  
  /* 购物车为空提示 */
  .empty-cart {
    text-align: center;
    font-size: 1.5em;
    color: #888;
  }
  
  /* 查看订单按钮 */
  .orders-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 12px 25px;
    font-size: 1.1em;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 30px;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  
  .orders-btn:hover {
    background-color: #0056b3;
  }
  </style>
  