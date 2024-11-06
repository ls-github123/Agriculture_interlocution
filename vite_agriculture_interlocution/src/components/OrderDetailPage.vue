<template>
    <div>
      <h1>订单详情</h1>
      <div v-if="order">
        <p>订单ID: {{ order.id }}</p>
        <p>总价: {{ order.total_price }}元</p>
        <p>创建时间: {{ order.created_at }}</p>
        <h3>订单商品:</h3>
        <div v-for="item in order.cart_items" :key="item.id" class="order-item">
          <p>{{ item.product.name }} - {{ item.quantity }} x {{ item.product.price }}元</p>
          <p>总价: {{ item.total_price }}元</p>
        </div>
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
  
          // 如果订单项中仅包含 product_id 而不包含商品的详细信息
          for (let item of this.order.cart_items) {
            const productResponse = await axios.get(`http://localhost:8000/api/products/${item.product_id}/`);
            item.product = productResponse.data;  // 假设返回的数据包含 product.name 和 product.price
            item.total_price = item.product.price * item.quantity;
          }
        } catch (error) {
          console.error('Failed to fetch order details:', error);
        }
      }
    }
  };
  </script>
  