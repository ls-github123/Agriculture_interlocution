<template>
  <!-- 搜索容器 -->
  <div class="search-container">
    <h1>科普农业大全</h1>
    <!-- 输入框绑定到 searchQuery 数据属性 -->
    <input type="text" v-model="searchQuery" placeholder="输入搜索内容..." />
    <!-- 搜索按钮触发 search 方法 -->
    <button @click="search">搜索</button>
    <!-- 如果正在加载数据，则显示加载中提示 -->
    <div v-if="loading" class="loading">
      <img :src="jiazai" alt="Loading..." /> <!-- 显示加载中的图片 -->
    </div>
    <!-- 如果数据加载完成，则显示结果  -->
    <div v-else>
      <!-- 循环渲染搜索结果 -->
      <div v-for="(item, index) in results" :key="index" class="result-item">
        <h3>{{ item.title }}</h3> <!-- 显示标题 -->
        <p>{{ item.content }}</p> <!-- 显示内容 -->
        <p>{{ item.category }}</p> <!-- 显示分类 -->
        <p>{{ item.author }}</p> <!-- 显示作者 -->
        <p>{{ item.tags }}</p> <!-- 显示标签 -->
      </div>
      <!-- 分页组件 -->
      <div class="pagination">
        <!-- 上一页按钮，当在第一页时禁用 -->
        <button :disabled="currentPage === 1" @click="prevPage">上一页</button>
        <!-- 当前页面信息 -->
        <span>第 {{ currentPage }} 页</span>
        <!-- 下一页按钮，当在最后一页时禁用 -->
        <button :disabled="currentPage === totalPages" @click="nextPage">下一页</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'; // 导入axios用于发送HTTP请求
import blobConfig from '../config/blobConfig';
import apiClient from '../utils/axios';



export default {
  name: 'loading',
  computed: {
    jiazai() {
      return `${blobConfig.baseBlobUrl}/gif/loading.gif`;
      }
    },
  data() {
    return {
      searchQuery: '', // 用户输入的搜索词
      results: [], // 存储搜索结果的数据数组
      loading: false, // 加载状态标志
      loadingStartedAt: null, // 加载开始时间
      minLoadingTime: 500, // 最小加载时间（毫秒）
      currentPage: 1, // 当前页面编号
      pageSize: 4, // 每页显示的结果数量
      totalPages: 1 // 总页数
    };
  },
  methods: {
    // 发起搜索请求的方法
    async search() {
      this.loading = true; // 设置加载状态为true
      this.loadingStartedAt = new Date().getTime(); // 记录加载开始时间
      try {
        // 发送GET请求到后端API获取搜索结果
        const response = await apiClient.get('/essearch/search', {
          params: {
            page: this.currentPage, // 请求的页码
            page_size: this.pageSize, // 每页大小
            mes: this.searchQuery // 用户输入的搜索词
          }
        });
        this.results = response.data.data; // 将返回的数据存入results数组
        this.totalPages = Math.ceil(response.data.total / this.pageSize); // 计算总页数
      } catch (error) {
        console.error('搜索失败:', error); // 捕获并打印错误信息
      }
      // 计算已加载的时间
      const elapsed = new Date().getTime() - this.loadingStartedAt;
      // 如果加载时间小于最小加载时间，则等待剩余时间后再结束加载状态
      if (elapsed < this.minLoadingTime) {
        setTimeout(() => {
          this.loading = false;
        }, this.minLoadingTime - elapsed);
      } else {
        this.loading = false; // 结束加载状态
      }
    },
    // 跳转到上一页的方法
    prevPage() {
      if (this.currentPage > 1) { // 只有当前不是第一页时才允许跳转
        this.currentPage--; // 页面编号减一
        this.search(); // 重新发起搜索请求
      }
    },
    // 跳转到下一页的方法
    nextPage() {
      if (this.currentPage < this.totalPages) { // 只有当前不是最后一页时才允许跳转
        this.currentPage++; // 页面编号加一
        this.search(); // 重新发起搜索请求
      }
    }
  }
};
</script>

<!-- 样式部分 -->
<style scoped>
.search-container {
  margin: 50px auto; /* 容器居中 */
  width: 700px; /* 调整宽度 */
  padding: 20px; /* 添加内边距 */
  background-color: #fff; /* 背景颜色 */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  border-radius: 8px; /* 圆角 */
  text-align: center; /* 文本居中 */
}

input {
  padding: 12px; /* 增加内边距 */
  width: 70%; /* 宽度占70% */
  margin-right: 10px; /* 右外边距 */
  border: 1px solid #ced4da; /* 边框颜色 */
  border-radius: 4px; /* 圆角 */
  font-size: 14px; /* 字体大小 */
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out; /* 平滑过渡 */
}

input:focus {
  border-color: #80bdff; /* 聚焦时边框颜色 */
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25); /* 聚焦时阴影效果 */
  outline: none; /* 去掉默认轮廓线 */
}

button {
  padding: 12px 24px; /* 增加内边距 */
  background-color: #007bff; /* 背景颜色 */
  color: #fff; /* 文字颜色 */
  border: none; /* 移除边框 */
  cursor: pointer; /* 鼠标悬停时指针变为手型 */
  margin: 5px; /* 外边距 */
  border-radius: 4px; /* 圆角 */
  font-size: 14px; /* 字体大小 */
  transition: background-color 0.15s ease-in-out; /* 平滑过渡 */
}

button:hover {
  background-color: #0056b3; /* 鼠标悬停时背景颜色变化 */
}

button:disabled {
  background-color: #6c757d; /* 按钮禁用时背景颜色 */
  cursor: not-allowed; /* 鼠标悬停时指针变为禁止符号 */
}

.loading {
  margin-top: 20px; /* 上方外边距 */
  font-size: 18px; /* 字体大小 */
  color: #6c757d; /* 字体颜色 */
}

.loading img {
  width: 160px; /* 图像宽度 */
  height: 160px; /* 图像高度 */
}

.result-item {
  border: 1px solid #e2e6ea; /* 边框颜色 */
  padding: 15px; /* 增加内边距 */
  margin: 15px 0; /* 上下外边距 */
  border-radius: 8px; /* 圆角 */
  background-color: #f8f9fa; /* 背景颜色 */
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  transition: box-shadow 0.2s ease-in-out; /* 平滑过渡 */
}

.result-item:hover {
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16); /* 鼠标悬停时阴影效果 */
}

.result-item h3 {
  margin: 0; /* 去除默认上下外边距 */
  font-size: 18px; /* 字体大小 */
  color: #343a40; /* 字体颜色 */
}

.result-item p {
  margin: 5px 0 0; /* 上方外边距 */
  font-size: 14px; /* 字体大小 */
  color: #6c757d; /* 字体颜色 */
}

.pagination {
  margin-top: 20px; /* 上方外边距 */
  display: flex; /* 使用弹性布局 */
  justify-content: space-between; /* 按钮之间留有空间 */
  align-items: center; /* 垂直居中 */
}

.pagination span {
  font-size: 16px; /* 字体大小 */
  color: #343a40; /* 字体颜色 */
}
</style>