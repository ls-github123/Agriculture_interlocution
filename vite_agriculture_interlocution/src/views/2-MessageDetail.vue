<template>
  <div class="message-detail">
    <!-- 导航栏 -->
    <van-nav-bar :title="pageTitle" left-text="返回" left-arrow @click-left="goBack">
      <template #right>
        <img src="/images/transparent-icon.gif" alt="Toggle Transparency" class="toggle-icon" @click="toggleTransparency" />
      </template>
    </van-nav-bar>

    <!-- 消息容器 -->
    <div class="message-container">
      <header class="message-header" :style="{ backgroundColor: isTransparent ? 'transparent' : 'rgba(255, 255, 255, 1)' }">
        <h1 class="message-title">{{ message.title }}</h1>
        <time class="message-time">{{ message.sent_at_formatted }}</time>
      </header>
      <div class="message-content-wrapper" :style="{ backgroundColor: isTransparent ? 'transparent' : 'rgba(255, 255, 255, 1)' }">
        <p class="message-content">{{ message.content }}</p>
      </div>
      <footer class="message-status">
        <van-tag type="warning">{{ getMessageStatusText(message.status) }}</van-tag>
      </footer>
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
    const isTransparent = ref(false); // 默认不透明

    // 计算属性：根据路由参数设置页面标题
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

    // 获取消息详细信息
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
        const data = response.data;

        // 处理时间格式
        if (data.sent_at) {
          const date = new Date(data.sent_at);
          data.sent_at_formatted = `${date.getFullYear()}年${date.getMonth() + 1}月${date.getDate()}日 ${date.getHours()}:${date.getMinutes()}`;
        }

        message.value = data;
      } catch (error) {
        Toast('加载消息详情失败');
        console.error('Error fetching message detail:', error);
      }
    };

    // 获取消息状态的文本描述
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

    // 页面加载时获取消息详细信息
    onMounted(() => {
      fetchMessageDetail();
    });

    // 返回上一页
    const goBack = () => {
      router.back();
    };

    // 切换背景透明度
    const toggleTransparency = () => {
      isTransparent.value = !isTransparent.value;
    };

    return {
      message,
      pageTitle,
      goBack,
      getMessageStatusText,
      isTransparent,
      toggleTransparency
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

.van-nav-bar {
  background: linear-gradient(to right, #3a6073, #ffffff); /* 左右渐变色 */
  color: white;
  border-radius: 20px; /* 圆角边框 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  overflow: hidden;
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
  flex-direction: column; /* 垂直排列 */
  align-items: center; /* 水平居中 */
  margin-bottom: 8px;
  transition: background-color 0.3s; /* 平滑过渡效果 */
}

.message-title {
  font-size: 18px;
  font-weight: bold;
  color: var(--primary-color);
  text-align: center; /* 标题居中 */
  margin: 0; /* 移除默认的上下外边距 */
}

.message-time {
  font-size: 14px;
  color: var(--secondary-color);
  text-align: center; /* 时间居中 */
  margin-top: 4px; /* 与标题的间距 */
  margin-bottom: 8px; /* 与内容的间距 */
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
  text-align: center; /* 内容居中 */
}

.message-status {
  margin-bottom: 8px;
  text-align: center; /* 状态居中 */
}

.toggle-icon {
  cursor: pointer;
  width: 24px;
  height: 24px;
}
</style>