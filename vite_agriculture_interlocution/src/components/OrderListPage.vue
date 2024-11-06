<template>
    <div>
      <h1>订单列表</h1>
      <div v-if="orders.length > 0">
        <div v-for="order in orders" :key="order.id" class="order-item">
          <p>订单ID: {{ order.id }} - 总价: {{ order.total_price }}元</p>
          <button @click="viewOrderDetails(order.id)">查看详情</button>
          
        </div>
      </div>
      <p v-else>没有订单</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        orders: []
      };
    },
    created() {
      this.fetchOrders();
    },
    methods: {
      // 获取订单列表
      async fetchOrders() {
        try {
          const response = await axios.get('http://localhost:8000/api/orders/');
          this.orders = response.data;
        } catch (error) {
          console.error('Failed to fetch orders:', error);
        }
      },
  
      // 查看订单详情
      viewOrderDetails(orderId) {
        this.$router.push({ name: 'OrderDetailPage', params: { id: orderId } });
      },
  
      // 支付订单
      payOrder(orderId) {
        alert('支付功能暂未实现');
      }
    }
  };
  </script>
  