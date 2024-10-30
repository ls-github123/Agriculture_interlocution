<template>
  <div class="messages-page">
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
      // 逻辑处理：标记所有消息为已读
      messages.value.forEach(message => (message.unread = false));
      Toast.success('所有消息已标记为已读');
    };

    const navigateToFeedbackForm = () => {
      // 逻辑处理：跳转到问题反馈页面
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

.nav-bar-title {
  color: white;
  font-size: 18px;
  margin-left: 16px;
}

.nav-bar-right {
  display: flex;
  align-items: center;
  margin-right: 16px;
}

.nav-bar-icon {
  margin-right: 5px;
  vertical-align: middle;
}

.nav-bar-text {
  vertical-align: middle;
  color: white;
}

.van-cell-group {
  margin-top: 10px;
  flex-grow: 1; /* 使消息列表占据剩余空间 */
}

.van-cell {
  background-color: white;
  border-radius: 8px;
  margin-bottom: 10px;
  padding: 12px 16px;
}

.message-icon {
  width: 24px; /* 调整图片大小 */
  height: 24px; /* 调整图片大小 */
  margin-right: 10px;
  vertical-align: middle;
}

.message-title {
  font-size: 16px;
  color: #333;
  display: block;
  margin-bottom: 4px;
}

.message-content {
  font-size: 14px;
  color: #999;
}

.unread-dot {
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
}

.button-container {
  margin-top: 20px;
  text-align: center; /* 居中对齐按钮 */
}

/* 自定义按钮样式 */
.custom-button {
  background-color: #07c160; /* 绿色背景 */
  border: none; /* 去掉边框 */
  border-radius: 8px; /* 圆角边框 */
  color: white; /* 白色文字 */
  font-size: 16px; /* 文字大小 */
  padding: 12px 20px; /* 内边距 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  transition: all 0.3s ease; /* 平滑过渡效果 */
  width: 200px; /* 设置按钮宽度 */
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


<!-- <template>
  <div class="messages-page">
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
      { icon: '/images/service.gif', title: '服务通知', content: '空', to: '/service-notification', unread: true },
      { icon: '/images/weather.gif', title: '气象提醒', content: '强降雨预警', to: '/weather-reminder', unread: false },
      { icon: '/images/plant.gif', title: '种植消息', content: '空', to: '/go/planting', unread: true },
      { icon: '/images/like-comment.gif', title: '赞评消息', content: '空', to: '/go/like-comment', unread: false },
      { icon: '/images/system.gif', title: '系统通知', content: '空', to: '/go/system', unread: true },
    ]);

    const markAllAsRead = () => {
      // 逻辑处理：标记所有消息为已读
      messages.value.forEach(message => (message.unread = false));
      Toast.success('所有消息已标记为已读');
    };

    const navigateToFeedbackForm = () => {
      // 逻辑处理：跳转到问题反馈页面
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

.nav-bar-title {
  color: white;
  font-size: 18px;
  margin-left: 16px;
}

.nav-bar-right {
  display: flex;
  align-items: center;
  margin-right: 16px;
}

.nav-bar-icon {
  margin-right: 5px;
  vertical-align: middle;
}

.nav-bar-text {
  vertical-align: middle;
  color: white;
}

.van-cell-group {
  margin-top: 10px;
  flex-grow: 1; /* 使消息列表占据剩余空间 */
}

.van-cell {
  background-color: white;
  border-radius: 8px;
  margin-bottom: 10px;
  padding: 12px 16px;
}

.message-icon {
  width: 24px; /* 调整图片大小 */
  height: 24px; /* 调整图片大小 */
  margin-right: 10px;
  vertical-align: middle;
}

.message-title {
  font-size: 16px;
  color: #333;
  display: block;
  margin-bottom: 4px;
}

.message-content {
  font-size: 14px;
  color: #999;
}

.unread-dot {
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
}

.button-container {
  margin-top: 20px;
  text-align: center; /* 居中对齐按钮 */
}

/* 自定义按钮样式 */
.custom-button {
  background-color: #07c160; /* 绿色背景 */
  border: none; /* 去掉边框 */
  border-radius: 8px; /* 圆角边框 */
  color: white; /* 白色文字 */
  font-size: 16px; /* 文字大小 */
  padding: 12px 20px; /* 内边距 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  transition: all 0.3s ease; /* 平滑过渡效果 */
  width: 200px; /* 设置按钮宽度 */
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
</style> -->