<template>
  <div class="order-list">
    <!-- 返回上一页按钮 -->
    <button class="back-btn" @click="goBack">← 返回</button>

    <h1 class="title">订单列表</h1>
    
    <div v-if="orders.length > 0" class="orders-container">
      <div v-for="order in orders" :key="order.id" class="order-item">
        <div class="order-info">
          <p><strong>订单ID:</strong> {{ order.id }}</p>
          <p><strong>总价:</strong> {{ order.total_price }}元</p>
        </div>
        <div class="order-actions">
          <button class="view-btn" @click="viewOrderDetails(order.id)">查看详情</button>
          <!-- <button class="pay-btn" @click="payOrder(order.id)">支付</button> -->
        </div>
      </div>
    </div>
    
    <p v-else class="no-orders">没有订单</p>
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
.order-list {
  font-family: 'Arial', sans-serif;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
}

/* 返回上一页按钮 */
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
  margin-top: 60px; /* 增加顶部空间避免与返回按钮重叠 */
  margin-bottom: 30px;
}

/* 订单容器 */
.orders-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* 订单项 */
.order-item {
  display: flex;
  justify-content: space-between;
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease-in-out;
}

.order-item:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}

/* 订单信息 */
.order-info p {
  font-size: 1.2em;
  margin: 5px 0;
}

.order-info strong {
  color: #333;
}

/* 订单操作按钮 */
.order-actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

.view-btn, .pay-btn {
  padding: 10px 20px;
  font-size: 1.1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.view-btn {
  background-color: #007bff;
  color: white;
  border: none;
}

.view-btn:hover {
  background-color: #0056b3;
}

.pay-btn {
  background-color: #28a745;
  color: white;
  border: none;
}

.pay-btn:hover {
  background-color: #218838;
}

/* 没有订单的提示 */
.no-orders {
  text-align: center;
  font-size: 1.5em;
  color: #888;
}
</style>
