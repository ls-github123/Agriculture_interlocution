<template>
  <div class="go-page">
    <!-- 导航栏 -->
    <van-nav-bar :title="pageTitle" left-text="返回" left-arrow @click-left="goBack">
      <template #right>
        <img src="/images/holi-colors.gif" alt="Toggle Gradients" @click="toggleGradients" class="toggle-button" />
      </template>
    </van-nav-bar>

    <!-- 主要内容容器 -->
    <div class="main-content">
      <!-- 消息列表 -->
      <div v-if="messages.length > 0" class="message-list">
        <div v-for="msg in messages" :key="msg.id" :class="['message-container', showGradients ? 'with-gradient' : '']" :style="getGradientStyle(msg.id)">
          <div class="message-header">
            <span class="message-title">{{ msg.title }}</span>
            <time class="message-time">{{ msg.sent_at_formatted }}</time>
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

      <!-- 没有消息时的提示 -->
      <div v-else class="no-message">
        暂无消息
      </div>
    </div>

    <!-- 分页控件 -->
    <div class="pagination-container">
      <van-pagination
        v-model="currentPage"
        :total-items="totalItems"
        :items-per-page="pageSize"
        @change="fetchMessages"
        class="custom-pagination"
      />
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted, computed, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { Toast } from 'vant';
import { Pagination as VanPagination, NavBar as VanNavBar } from 'vant';
import axios from 'axios';

export default {
  components: {
    'van-pagination': VanPagination,
    'van-nav-bar': VanNavBar,
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const messages = ref([]);
    const gradientStyles = ref({});
    const showGradients = ref(false);
    const previousGradientStyles = ref({});
    const currentPage = ref(1); // 当前页码
    const totalItems = ref(0); // 总条目数
    const pageSize = ref(4); // 每页显示的数量
    const isFetchingMore = ref(false); // 标志变量，用于区分滚动加载和分页加载   true

    // 计算属性：根据路由参数设置页面标题
    const pageTitle = computed(() => {
      switch (route.params.type) {
        case 'service':
          return '服务通知';
        case 'weather':
          return '气象提醒';
        case '种植消息':
          return '种植消息';
        case 'like-comment':
          return '赞评消息';
        case 'system':
          return '系统通知';
        default:
          return '消息';
      }
    });

    // 获取消息列表
    const fetchMessages = async (page = currentPage.value, append = false) => {
      try {
        let url = '';
        switch (route.params.type) {
          case 'service':
            url = `http://127.0.0.1:8000/messageModule/service-messages/?page=${page}&page_size=${pageSize.value}`;
            break;
          case 'weather':
            url = `http://127.0.0.1:8000/messageModule/weather-reminders/?page=${page}&page_size=${pageSize.value}`;
            break;
          case '种植消息':
            url = `http://127.0.0.1:8000/messageModule/planting-messages/?page=${page}&page_size=${pageSize.value}`;
            break;
          case 'like-comment':
            url = `http://127.0.0.1:8000/messageModule/praise-comment-messages/?page=${page}&page_size=${pageSize.value}`;
            break;
          case 'system':
            url = `http://127.0.0.1:8000/messageModule/system-notifications/?page=${page}&page_size=${pageSize.value}`;
            break;
          default:
            return;
        }
        const response = await axios.get(url);
        const data = response.data;

        // 处理时间格式
        data.results.forEach((msg) => {
          if (msg.sent_at) {
            const date = new Date(msg.sent_at);
            msg.sent_at_formatted = `${date.getFullYear()}年${date.getMonth() + 1}月${date.getDate()}日 ${date.getHours()}时${date.getMinutes()}分`;
          }
        });

        if (append) {
          // 追加新数据
          messages.value = [...messages.value, ...data.results];
        } else {
          // 替换现有数据
          messages.value = data.results;
        }

        totalItems.value = data.count; // 设置总条目数
      } catch (error) {
        Toast('加载消息失败');
        console.error('Error fetching messages:', error);
      }
    };

    // 查看消息详细信息
    const viewMessageDetail = (messageId) => {
      router.push({
        name: 'MessageDetail',
        params: { messageId },
        query: { type: route.params.type }
      });
    };

    // 标记消息为已读
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

    // 获取渐变样式
    const getGradientStyle = (id) => {
      return showGradients.value ? gradientStyles.value[id] : {};
    };

    // 生成渐变样式
    const generateGradientStyles = () => {
      messages.value.forEach((msg) => {
        let angle, hue1, hue2, gradient;
        do {
          angle = Math.floor(Math.random() * 360);
          hue1 = Math.floor(Math.random() * 360);
          hue2 = (hue1 + 180) % 360;
          gradient = `linear-gradient(${angle}deg, hsl(${hue1}, 70%, 50%), hsl(${hue2}, 70%, 50%))`;
        } while (previousGradientStyles.value[msg.id]?.background === gradient);

        gradientStyles.value[msg.id] = { background: gradient };
      });
    };

    // 切换渐变背景显示
    const toggleGradients = () => {
      showGradients.value = !showGradients.value;
      if (showGradients.value) {
        previousGradientStyles.value = { ...gradientStyles.value };
        generateGradientStyles();
      }
    };

    // 页面加载时获取消息列表
    onMounted(() => {
      fetchMessages();

      // 添加滚动事件监听器
      window.addEventListener('scroll', handleScroll);
    });

    // 移除滚动事件监听器
    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll);
    });

    // 处理滚动事件
    const handleScroll = () => {
      const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
      const windowHeight = document.documentElement.clientHeight || document.body.clientHeight;
      const scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;

      if (scrollTop + windowHeight >= scrollHeight && !isFetchingMore.value) {
        // 滚动到底部，加载更多数据
        isFetchingMore.value = true;
        currentPage.value += 1;
        fetchMessages(currentPage.value, true).then(() => {
          isFetchingMore.value = false;
        });
      }
    };

    // 返回上一页
    const goBack = () => {
      router.back();
    };

    // 监听 currentPage 的变化
    watch(currentPage, (newPage) => {
      if (!isFetchingMore.value) {
        fetchMessages(newPage, false);
      }
    });

    return {
      messages,
      pageTitle,
      goBack,
      markAsRead,
      viewMessageDetail,
      getMessageStatusText,
      getGradientStyle,
      showGradients,
      toggleGradients,
      currentPage,
      totalItems,
      pageSize,
      fetchMessages, // 确保返回 fetchMessages 方法
    };
  },
};
</script>

<style scoped>
.go-page {
  background-color: #f0f2f5; /* 浅灰色背景 */
  height: 100vh; /* 占满整个视口高度 */
  padding: 0 10px; /* 左右内边距 */
  display: flex; /* 使用 Flexbox 布局 */
  flex-direction: column; /* 垂直排列子元素 */
}

.van-nav-bar {
  background: linear-gradient(135deg, #ff7e5f, #feb47b); /* 渐变背景 */
  color: white; /* 文字颜色 */
  border-radius: 20px; /* 圆角边框 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  overflow: hidden; /* 隐藏溢出内容 */
}

.toggle-button {
  width: 24px; /* 图片宽度 */
  height: 24px; /* 图片高度 */
  cursor: pointer; /* 鼠标指针样式 */
}

.main-content {
  flex: 1; /* 使主要内容占据剩余空间 */
  overflow-y: auto; /* 添加垂直滚动条 */
  margin-top: 10px; /* 上边距 */
}

.message-list {
  margin-bottom: 20px; /* 下边距 */
}

.message-container {
  border-radius: 8px; /* 圆角边框 */
  margin-bottom: 10px; /* 下边距 */
  padding: 16px; /* 内边距 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.message-header {
  display: flex; /* 使用 Flexbox 布局 */
  justify-content: space-between; /* 两端对齐 */
  align-items: center; /* 垂直居中对齐 */
  margin-bottom: 8px; /* 下边距 */
}

.message-title {
  font-size: 18px; /* 字体大小 */
  font-weight: bold; /* 加粗 */
}

.message-time {
  font-size: 14px; /* 字体大小 */
  color: #666; /* 文字颜色 */
}

.message-content {
  font-size: 16px; /* 字体大小 */
  color: #333; /* 文字颜色 */
  margin-bottom: 8px; /* 下边距 */
}

.message-status {
  font-size: 14px; /* 字体大小 */
  color: #666; /* 文字颜色 */
}

.view-button {
  text-align: right; /* 文本右对齐 */
  margin-top: 8px; /* 上边距 */
}

.view-button button {
  background-color: #07c160; /* 背景色 */
  color: white; /* 文字颜色 */
  border: none; /* 去掉边框 */
  padding: 8px 16px; /* 内边距 */
  border-radius: 4px; /* 圆角边框 */
  cursor: pointer; /* 鼠标指针样式 */
  font-size: 14px; /* 字体大小 */
}

.view-button button:hover {
  background-color: #06b258; /* 鼠标悬停时的背景颜色 */
}

.no-message {
  text-align: center; /* 文本居中对齐 */
  font-size: 18px; /* 字体大小 */
  color: #999; /* 文字颜色 */
  margin-top: 20px; /* 上边距 */
}

.pagination-container {
  margin-top: 20px; /* 上边距 */
  text-align: center; /* 文本居中对齐 */
  padding: 10px 0; /* 内边距 */
  background-color: #fff; /* 背景颜色 */
  border-top: 1px solid #e0e0e0; /* 上边框 */
  box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.custom-pagination {
  display: inline-block; /* 使分页控件水平居中 */
}

.custom-pagination .van-pagination__item {
  background-color: #f5f5f5; /* 背景颜色 */
  color: #333; /* 文字颜色 */
  border: 1px solid #ddd; /* 边框颜色 */
  border-radius: 4px; /* 圆角边框 */
  padding: 5px 10px; /* 内边距 */
  margin: 0 5px; /* 外边距 */
  transition: all 0.3s ease; /* 平滑过渡效果 */
}

.custom-pagination .van-pagination__item--active {
  background-color: #07c160; /* 激活项的背景颜色 */
  color: #fff; /* 激活项的文字颜色 */
  border-color: #07c160; /* 激活项的边框颜色 */
}

.custom-pagination .van-pagination__item--disabled {
  opacity: 0.5; /* 禁用项的透明度 */
  cursor: not-allowed; /* 禁用项的鼠标指针样式 */
}
</style>