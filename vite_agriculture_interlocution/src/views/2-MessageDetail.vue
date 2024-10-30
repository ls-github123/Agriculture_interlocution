<template>
  <div class="message-detail">
    <van-nav-bar :title="pageTitle" left-text="返回" left-arrow @click-left="goBack" />
    <div class="message-container">
      <div class="message-header">
        <span class="message-title">{{ message.title }}</span>
        <span class="message-time">{{ message.sent_at_formatted }}</span>
      </div>
      <div class="message-content">
        {{ message.content }}
      </div>
      <div class="message-status">
        状态: {{ getMessageStatusText(message.status) }}
      </div>
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
    const message = ref({});

    const pageTitle = computed(() => {
      switch (route.query.type) {
        case 'service':
          return '服务通知详情';
        case 'weather':
          return '气象提醒详情';
        case 'planting':
          return '种植消息详情';
        case 'like-comment':
          return '赞评消息详情';
        case 'system':
          return '系统通知详情';
        default:
          return '消息详情';
      }
    });

    const fetchMessageDetail = async () => {
      try {
        let url = '';
        switch (route.query.type) {
          case 'service':
            url = `http://127.0.0.1:8000/messageModule/service-messages/${route.params.messageId}/`;
            break;
          case 'weather':
            url = `http://127.0.0.1:8000/messageModule/weather-reminders/${route.params.messageId}/`;
            break;
          case 'planting':
            url = `http://127.0.0.1:8000/messageModule/planting-messages/${route.params.messageId}/`;
            break;
          case 'like-comment':
            url = `http://127.0.0.1:8000/messageModule/praise-comment-messages/${route.params.messageId}/`;
            break;
          case 'system':
            url = `http://127.0.0.1:8000/messageModule/system-notifications/${route.params.messageId}/`;
            break;
          default:
            return;
        }
        const response = await axios.get(url);
        message.value = response.data;
      } catch (error) {
        Toast('加载消息详情失败');
        console.error('Error fetching message detail:', error);
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
      fetchMessageDetail();
    });

    const goBack = () => {
      router.back();
    };

    return {
      message,
      pageTitle,
      goBack,
      getMessageStatusText
    };
  },
};
</script>

<style scoped>
.message-detail {
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

.message-container {
  background-color: white;
  border-radius: 8px;
  margin-top: 10px;
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
  color: #999;
}
</style>


<!-- <template>
  <div class="message-detail">
    <van-nav-bar title="消息详情" left-text="返回" left-arrow @click-left="goBack">
      <template #right>
        <img src="/images/transparent-icon.gif" alt="Toggle Transparency" class="toggle-icon" @click="toggleTransparency" />
      </template>
    </van-nav-bar>

    <div class="message-container">
      <header class="message-header" :style="{ backgroundColor: isTransparent ? 'transparent' : 'rgba(255, 255, 255, 1)' }">
        <h1 class="message-title">{{ message.title }}</h1>
        <time class="message-time">{{ message.send_time_formatted }}</time>
      </header>
      <div class="message-content-wrapper" :style="{ backgroundColor: isTransparent ? 'transparent' : 'rgba(255, 255, 255, 1)' }">
        <p class="message-content">{{ message.content }}</p>
      </div>
      <footer class="message-type">
        <van-tag type="warning">{{ message.type_id?.type_name || '未知类型' }}</van-tag>
      </footer>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { Toast } from 'vant';
import axios from 'axios';

export default {
  setup() {
    const route = useRoute();
    const message = ref({});
    const isTransparent = ref(false); // 默认不透明

    const fetchMessage = async () => {
      try {
        const messageId = route.params.messageId;
        const messageType = route.query.type; // 获取消息类型
        let url = '';

        switch (messageType) {
          case 'planting':
            url = `http://127.0.0.1:8000/messageModule/planting-messages/${messageId}/`;
            break;
          case 'like-comment':
            url = `http://127.0.0.1:8000/messageModule/like-comment-messages/${messageId}/`;
            break;
          case 'system':
            url = `http://127.0.0.1:8000/messageModule/system-notifications/${messageId}/`;
            break;
          default:
            throw new Error('Unknown message type');
        }

        const response = await axios.get(url);
        message.value = response.data;
      } catch (error) {
        Toast('加载消息详情失败');
        console.error('Error fetching message detail:', error);
      }
    };

    onMounted(() => {
      fetchMessage();
    });

    const goBack = () => {
      window.history.back();
    };

    const toggleTransparency = () => {
      isTransparent.value = !isTransparent.value;
    };

    return {
      message,
      goBack,
      isTransparent,
      toggleTransparency,
    };
  },
};
</script>

<style scoped>
:root {
  --primary-color: #333;
  --secondary-color: #666;
  --background-color: #fff;
  --border-radius: 8px;
  --padding: 16px;
}

.message-detail {
  display: flex;
  flex-direction: column;
  height: 100vh; /* 设置高度为视口高度 */
  padding: var(--padding);
  background-image: url('/images/144.jpg'); /* 确保图片路径正确 */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed; /* 背景图片固定 */
  position: relative; /* 为遮罩层设置相对定位 */
  overflow: hidden; /* 防止内容溢出 */
}

.message-container {
  flex: 1; /* 使内容容器占据剩余空间 */
  display: flex;
  flex-direction: column;
  background-color: var(--background-color);
  border-radius: var(--border-radius);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: var(--padding);
  margin-bottom: 20px;
  overflow: hidden; /* 防止内容溢出 */
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  transition: background-color 0.3s; /* 平滑过渡效果 */
}

.message-title {
  font-size: 18px;
  font-weight: bold;
  color: var(--primary-color);
}

.message-time {
  font-size: 14px;
  color: var(--secondary-color);
}

.message-content-wrapper {
  flex: 1; /* 使内容区域占据剩余空间 */
  overflow-y: auto; /* 当内容超过显示区域时显示垂直滚动条 */
  padding: var(--padding);
  border-radius: var(--border-radius);
  margin-bottom: 8px;
  transition: background-color 0.3s; /* 平滑过渡效果 */
}

.message-content {
  font-size: 16px;
  color: var(--primary-color);
  white-space: pre-line; /* 保留换行符 */
}

.message-type {
  margin-bottom: 8px;
}

.toggle-icon {
  cursor: pointer;
  width: 24px;
  height: 24px;
}
</style> -->