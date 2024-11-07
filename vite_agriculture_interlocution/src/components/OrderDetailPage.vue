<template>
  <div class="order-detail-page">
    <!-- 返回按钮 -->
    <button class="back-btn" @click="goBack">← 返回</button>

    <h1 class="title">订单详情</h1>

    <div v-if="order" class="order-details-container">
      <p><strong>订单ID:</strong> {{ order.id }}</p>
      <p><strong>总价:</strong> {{ order.total_price }}元</p>
      <p><strong>生成订单时间:</strong> {{ formatDate(order.created_at) }}</p>

      <div class="order-items-container">
        <h3>订单商品</h3>
        <div v-for="item in order.cart_items" :key="item.id" class="order-item">
          <p><strong>{{ item.product.name }}</strong> - {{ item.quantity }} x {{ item.product.price }}元</p>
          <p><strong>总价:</strong> {{ item.total_price }}元</p>
        </div>
      </div>

      <button class="pay-btn" @click="pay">订单支付</button>
    </div>

    <p v-else class="no-order">没有找到订单</p>
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
        const response = await axios.get(`http://localhost:8000/agri_cart/orders/${orderId}/`);
        this.order = response.data;
      } catch (error) {
        console.error('Failed to fetch order details:', error);
      }
    },

    // 格式化日期为 YYYY-MM-DD
    formatDate(dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const seconds = date.getSeconds().toString().padStart(2, '0');
    
    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
  },

    // 调用支付接口，跳转支付宝支付页面
    async pay() {
      try {
        const response = await axios.post(`http://localhost:8000/agri_cart/alipay/${this.id}/`);
        window.location.href = response.data.pay_url;  // 跳转到支付宝支付页面
      } catch (error) {
        console.error('Failed to initiate payment:', error);
      }
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
.order-detail-page {
  font-family: 'Arial', sans-serif;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
}

/* 返回按钮 */
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

/* 订单详情容器 */
.order-details-container {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* 订单商品容器 */
.order-items-container {
  margin-top: 20px;
}

.order-item {
  background-color: #f8f9fa;
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 5px;
}

.order-item p {
  font-size: 1.2em;
  margin: 5px 0;
}

.order-item strong {
  color: #333;
}

/* 支付按钮 */
.pay-btn {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 12px 25px;
  font-size: 1.2em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 30px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.pay-btn:hover {
  background-color: #218838;
}

/* "没有订单"提示 */
.no-order {
  text-align: center;
  font-size: 1.5em;
  color: #888;
}
</style>
