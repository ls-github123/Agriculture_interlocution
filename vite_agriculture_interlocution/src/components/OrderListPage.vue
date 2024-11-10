<template>
  <div class="order-list">
    <!-- 返回上一页按钮 -->
    <button class="back-btn" @click="goBack">← 返回</button>

    <h1 class="title">订单列表</h1>

    <!-- 切换当前订单和历史订单 -->
    <div class="tabs">
      <button
        class="tab-btn"
        :class="{ active: activeTab === 'current' }"
        @click="activeTab = 'current'"
      >
        当前订单
      </button>
      <button
        class="tab-btn"
        :class="{ active: activeTab === 'history' }"
        @click="activeTab = 'history'"
      >
        历史订单
      </button>
    </div>

    <!-- 当前订单列表 -->
    <div v-if="activeTab === 'current'">
      <div v-if="currentOrders.length > 0" class="orders-container">
        <div v-for="order in currentOrders" :key="order.id" class="order-item">
          <div class="order-info">
            <p><strong>订单ID:</strong> {{ order.id }}</p>
            <p><strong>总价:</strong> {{ order.total_price }}元</p>
          </div>
          <div class="order-actions">
            <button class="view-btn" @click="viewOrderDetails(order.id)">查看详情</button>
            <button class="pay-btn" @click="payOrder(order.id)">支付</button>
          </div>
        </div>
      </div>
      <p v-else class="no-orders">没有当前订单</p>
    </div>

    <!-- 历史订单列表 -->
    <div v-if="activeTab === 'history'">
      <div v-if="historyOrders.length > 0" class="orders-container">
        <div v-for="order in historyOrders" :key="order.id" class="order-item">
          <div class="order-info">
            <p><strong>订单ID:</strong> {{ order.id }}</p>
            <p><strong>总价:</strong> {{ order.total_price }}元</p>
          </div>
          <div class="order-actions">
            <button class="view-btn" @click="viewOrderDetails(order.id)">查看详情</button>
          </div>
        </div>
      </div>
      <p v-else class="no-orders">没有历史订单</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const activeTab = ref('current');
    const currentOrders = ref([]);
    const historyOrders = ref([]);

    // 获取当前订单和历史订单
    const fetchOrders = async () => {
      try {
        const response = await axios.get('http://localhost:8000/agri_cart/orders/');
        // 先获取所有订单，并根据 paid 字段分成当前订单和历史订单
        const orders = response.data;

        currentOrders.value = orders.filter(order => !order.paid).sort((a, b) => {
          return new Date(b.date) - new Date(a.date); // 按日期倒序排序
        });

        historyOrders.value = orders.filter(order => order.paid).sort((a, b) => {
          return new Date(b.date) - new Date(a.date); // 按日期倒序排序
        });

      } catch (error) {
        console.error('Failed to fetch orders:', error);
      }
    };

    // 视图加载时获取订单数据
    onMounted(() => {
      fetchOrders();
    });

    // 查看订单详情
    const viewOrderDetails = (orderId) => {
      console.log('查看订单ID:', orderId);
      // 示例：可以使用 vue-router 跳转到订单详情页面
      // this.$router.push({ name: 'OrderDetailPage', params: { id: orderId } });
    };

    // 支付订单
    const payOrder = (orderId) => {
      alert('支付功能暂未实现');
    };

    // 返回上一页
    const goBack = () => {
      window.history.back();
    };

    return {
      activeTab,
      currentOrders,
      historyOrders,
      viewOrderDetails,
      payOrder,
      goBack,
    };
  },
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
  margin-top: 60px;
  margin-bottom: 30px;
}

/* 标签样式 */
.tabs {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 20px;
}

.tab-btn {
  padding: 10px 20px;
  font-size: 1.2em;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
}

.tab-btn.active {
  background-color: #0056b3;
}

.tab-btn:hover {
  background-color: #0056b3;
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

.view-btn,
.pay-btn {
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
