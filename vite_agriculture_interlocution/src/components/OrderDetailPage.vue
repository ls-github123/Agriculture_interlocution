<template>
    <div>
      <h1>订单详情</h1>
      <div v-if="order">
        <p>订单ID: {{ order.id }}</p>
        <p>总价: {{ order.total_price }}元</p>
        <p>创建时间: {{ order.created_at }}</p>
        <!-- <h3>订单</h3> -->
        <div v-for="item in order.cart_items" :key="item.id" class="order-item">
          <p>{{ item.product.name }} - {{ item.quantity }} x {{ item.product.price }}元</p>
          <p>总价: {{ item.total_price }}元</p>
        </div>
        <button @click="pay">订单支付</button>
      </div>
      <p v-else>没有找到订单</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: ['id'],  // 接收路由传递的id参数
  
    data() {
      return {
        order: null
      };
    },
  
    created() {
      if (this.id) {
        this.fetchOrderDetails(this.id);
      }
    },
  
    methods: {
      // 获取订单详情
      async fetchOrderDetails(orderId) {
        try {
          const response = await axios.get(`http://localhost:8000/api/orders/${orderId}/`);
          this.order = response.data;
        } catch (error) {
          console.error('Failed to fetch order details:', error);
        }
      },
  
      // 调用支付接口，跳转支付宝支付页面
      async pay() {
        try {
          const response = await axios.post(`http://localhost:8000/api/alipay/${this.id}/`);
          window.location.href = response.data.pay_url;  // 跳转到支付宝支付页面
        } catch (error) {
          console.error('Failed to initiate payment:', error);
        }
      }
    }
  };
  </script>
  