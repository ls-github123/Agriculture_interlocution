<template>
  <div class="go-page">
    <van-nav-bar :title="pageTitle" left-text="返回" left-arrow @click-left="goBack" />

    <div v-if="messages.length > 0" class="message-list">
      <div v-for="msg in messages" :key="msg.id" class="message-container">
        <div class="message-header">
          <span class="message-title">{{ msg.title }}</span>
          <span class="message-time">{{ msg.sent_at_formatted }}</span>
        </div>
        <div class="message-content">
          {{ msg.content }}
        </div>
        <div class="message-status">
          状态: {{ getMessageStatusText(msg.status) }}
        </div>
        <div class="view-button">
          <button @click="viewMessageDetail(msg.id)">查看详情</button>
        </div>
      </div>
    </div>

    <div v-else class="no-message">
      暂无消息
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { Toast } from 'vant';
import axios from 'axios';

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const messages = ref([]);

    const pageTitle = computed(() => {
      switch (route.params.type) {
        case 'service':
          return '服务通知';
        case 'weather':
          return '气象提醒';
        case 'planting':
          return '种植消息';
        case 'like-comment':
          return '赞评消息';
        case 'system':
          return '系统通知';
        default:
          return '消息';
      }
    });

    const fetchMessages = async () => {
      try {
        let url = '';
        switch (route.params.type) {
          case 'service':
            url = `http://127.0.0.1:8000/messageModule/service-messages/`;
            break;
          case 'weather':
            url = `http://127.0.0.1:8000/messageModule/weather-reminders/`;
            break;
          case 'planting':
            url = `http://127.0.0.1:8000/messageModule/planting-messages/`;
            break;
          case 'like-comment':
            url = `http://127.0.0.1:8000/messageModule/praise-comment-messages/`;
            break;
          case 'system':
            url = `http://127.0.0.1:8000/messageModule/system-notifications/`;
            break;
          default:
            return;
        }
        const response = await axios.get(url);
        messages.value = response.data; // 将整个数组赋值给 messages
      } catch (error) {
        Toast('加载消息失败');
        console.error('Error fetching messages:', error);
      }
    };

    const viewMessageDetail = (messageId) => {
      router.push({
        name: 'MessageDetail',
        params: { messageId },
        query: { type: route.params.type }
      });
    };

    const markAsRead = async (msg) => {
      try {
        const url = `http://127.0.0.1:8000/messageModule/mark-as-read/`;
        await axios.post(url, { type: route.params.type, message_id: msg.id });
        msg.status = 'read';
        Toast.success('消息已标记为已读');
      } catch (error) {
        Toast('标记为已读失败');
        console.error('Error marking message as read:', error);
      }
    };

    const getMessageStatusText = (status) => {
      switch (status) {
        case 'unread':
          return '未读';
        case 'read':
          return '已读';
        case 'deleted':
          return '已删除';
        default:
          return '未知状态';
      }
    };

    onMounted(() => {
      fetchMessages();
    });

    const goBack = () => {
      router.back();
    };

    return {
      messages,
      pageTitle,
      goBack,
      markAsRead,
      viewMessageDetail,
      getMessageStatusText
    };
  },
};
</script>

<style scoped>
.go-page {
  background-color: #f0f2f5; /* 浅灰色背景 */
  height: 100vh;
  padding: 0 10px;
  display: flex;
  flex-direction: column;
}

.van-nav-bar {
  background-color: hwb(166 61% 3% / 0.718);
  color: white;
  border-radius: 20px; /* 圆角边框 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  overflow: hidden;
}

.message-list {
  margin-top: 10px;
  flex: 1; /* 使 message-list 占据剩余空间 */
  overflow-y: auto; /* 添加垂直滚动条 */
}

.message-container {
  background-color: white;
  border-radius: 8px;
  margin-bottom: 10px;
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
}

.message-status {
  font-size: 14px;
  color: #666;
}

.view-button {
  text-align: right;
  margin-top: 8px;
}

.view-button button {
  background-color: #07c160;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.view-button button:hover {
  background-color: #06b258;
}

.no-message {
  text-align: center;
  font-size: 18px;
  color: #999;
  margin-top: 20px;
}
</style>

