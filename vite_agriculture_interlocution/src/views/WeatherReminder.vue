<template>
  <div class="message-list">
    <van-nav-bar title="气象提醒" left-text="返回" left-arrow @click-left="goBack" />

    <div v-if="messages.length === 0" class="no-messages">
      暂无消息
    </div>

    <div class="message-item" v-for="message in messages" :key="message.message_id">
      <div class="message-header">
        <span class="message-title">{{ message.title }}</span>
        <span class="message-time">{{ message.send_time_formatted }}</span>
      </div>
      <div class="message-content">
        {{ message.content }}
      </div>
      <div class="message-type">
        <van-tag type="warning">{{ message.type_id?.type_name || '未知类型' }}</van-tag>
      </div>
      <div class="view-link">
        <router-link :to="{ name: 'MessageDetail', params: { messageId: message.message_id } }">点击查看</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { Toast } from 'vant';
import axios from 'axios';

export default {
  setup() {
    const messages = ref([]);

    const fetchMessages = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/messageModule/messages/');
        messages.value = response.data;
      } catch (error) {
        Toast('加载消息失败');  // 使用 Toast 的 text 方法
        console.error('Error fetching messages:', error);
      }
    };

    onMounted(() => {
      fetchMessages();
    });

    const goBack = () => {
      window.history.back();
    };

    return {
      messages,
      goBack,
    };
  },
};
</script>

<style scoped>
.message-list {
  padding: 16px;
}

.no-messages {
  text-align: center;
  font-size: 18px;
  color: #999;
  margin-top: 20px;
}

.message-item {
  background-color: #fff;
  border-radius: 8px;
  margin-bottom: 16px;
  padding: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.message-title {
  font-size: 18px;
  font-weight: bold;
}

.message-time {
  font-size: 14px;
  color: #666;
}

.message-content {
  font-size: 16px;
  color: #333;
  margin-bottom: 8px;
  white-space: nowrap; /* 不换行 */
  overflow: hidden; /* 超出部分隐藏 */
  text-overflow: ellipsis; /* 超出部分显示省略号 */
  max-width: 100%; /* 最大宽度 */
}

.message-type {
  margin-bottom: 8px;
}

.view-link a {
  color: #1989fa;
  text-decoration: none;
}
</style>