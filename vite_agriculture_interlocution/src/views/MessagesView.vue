<template>
  <div class="messages-page">
    <!-- 导航栏 -->
    <van-nav-bar @click-right="navigateToFeedbackForm">
      <template #left>
        <span class="nav-bar-title">消息</span>
      </template>
      <template #right>
        <div class="nav-bar-right">
          <van-icon name="question-o" size="18" class="nav-bar-icon" />
          <span class="nav-bar-text">问题反馈</span>
        </div>
      </template>
    </van-nav-bar>

    <!-- 消息列表 -->
    <van-cell-group>
      <van-cell v-for="(message, index) in messages" :key="index" :to="message.to" is-link>
        <template #icon>
          <img :src="message.icon" alt="icon" class="message-icon" />
        </template>
        <template #title>
          <span class="message-title">{{ message.title }}</span>
        </template>
        <template #label>
          <span class="message-content">{{ message.content }}</span>
        </template>
        <template #default>
          <van-tag v-if="message.unread" round color="#f44" class="unread-dot" />
        </template>
      </van-cell>
    </van-cell-group>

    <!-- 全部已读按钮 -->
    <div class="button-container">
      <van-button type="primary" @click="markAllAsRead" class="custom-button">全部已读</van-button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { Toast } from 'vant';
import { Icon, NavBar, Cell, CellGroup, Button, Tag } from 'vant';

export default {
  components: {
    'van-icon': Icon,
    'van-nav-bar': NavBar,
    'van-cell': Cell,
    'van-cell-group': CellGroup,
    'van-button': Button,
    'van-tag': Tag,
  },
  setup() {
    const router = useRouter();
    const messages = ref([
      { icon: '/images/service.gif', title: '服务通知', content: '空', to: '/go/service', unread: true },
      { icon: '/images/weather.gif', title: '气象提醒', content: '强降雨预警', to: '/go/weather', unread: false },
      { icon: '/images/plant.gif', title: '种植消息', content: '空', to: '/go/planting', unread: true },
      { icon: '/images/like-comment.gif', title: '赞评消息', content: '空', to: '/go/like-comment', unread: false },
      { icon: '/images/system.gif', title: '系统通知', content: '空', to: '/go/system', unread: true },
    ]);

    const markAllAsRead = () => {
      // 标记所有消息为已读
      messages.value.forEach(message => (message.unread = false));
      // 显示成功提示
      Toast.success('所有消息已标记为已读');
    };

    const navigateToFeedbackForm = () => {
      // 跳转到问题反馈页面
      router.push('/feedback-form');
    };

    return {
      messages,
      markAllAsRead,
      navigateToFeedbackForm,
    };
  },
};
</script>

<style scoped>
.messages-page {
  background-color: #f0f2f5; /* 浅灰色背景 */
  height: 100vh; /* 占满整个视口高度 */
  padding: 0 10px; /* 左右内边距 */
  display: flex; /* 使用 Flexbox 布局 */
  flex-direction: column; /* 垂直排列子元素 */
}

.van-nav-bar {
  background: linear-gradient(135deg, #256280, #6b98af); /* 渐变背景 */
  color: white; /* 文字颜色 */
  border-radius: 20px; /* 圆角边框 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  overflow: hidden; /* 隐藏溢出内容 */
}

.nav-bar-title {
  color: white; /* 文字颜色 */
  font-size: 18px; /* 字体大小 */
  margin-left: 16px; /* 左边距 */
}

.nav-bar-right {
  display: flex; /* 使用 Flexbox 布局 */
  align-items: center; /* 垂直居中对齐 */
  margin-right: 16px; /* 右边距 */
}

.nav-bar-icon {
  margin-right: 5px; /* 右边距 */
  vertical-align: middle; /* 垂直居中对齐 */
}

.nav-bar-text {
  vertical-align: middle; /* 垂直居中对齐 */
  color: white; /* 文字颜色 */
}

.van-cell-group {
  margin-top: 10px; /* 上边距 */
  flex-grow: 1; /* 使消息列表占据剩余空间 */
}

.van-cell {
  background-color: white; /* 背景色 */
  border-radius: 8px; /* 圆角边框 */
  margin-bottom: 10px; /* 下边距 */
  padding: 12px 16px; /* 内边距 */
}

.message-icon {
  width: 24px; /* 图标宽度 */
  height: 24px; /* 图标高度 */
  margin-right: 10px; /* 右边距 */
  vertical-align: middle; /* 垂直居中对齐 */
}

.message-title {
  font-size: 16px; /* 字体大小 */
  color: #333; /* 文字颜色 */
  display: block; /* 块级元素 */
  margin-bottom: 4px; /* 下边距 */
}

.message-content {
  font-size: 14px; /* 字体大小 */
  color: #999; /* 文字颜色 */
}

.unread-dot {
  position: absolute; /* 绝对定位 */
  right: 16px; /* 右边距 */
  top: 50%; /* 顶部居中 */
  transform: translateY(-50%); /* 垂直居中对齐 */
}

.button-container {
  margin-top: 20px; /* 上边距 */
  text-align: center; /* 文本居中对齐 */
}

/* 自定义按钮样式 */
.custom-button {
  background-color: #07c160; /* 背景色 */
  border: none; /* 去掉边框 */
  border-radius: 8px; /* 圆角边框 */
  color: white; /* 文字颜色 */
  font-size: 16px; /* 字体大小 */
  padding: 12px 20px; /* 内边距 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  transition: all 0.3s ease; /* 平滑过渡效果 */
  width: 200px; /* 按钮宽度 */
  display: inline-block; /* 使按钮居中对齐 */
}

.custom-button:hover {
  background-color: #05a64e; /* 鼠标悬停时的背景颜色 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 鼠标悬停时的阴影效果 */
}

.custom-button:active {
  background-color: #048c46; /* 按下时的背景颜色 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 按下时的阴影效果 */
}
</style>