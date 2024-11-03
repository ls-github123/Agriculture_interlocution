<template>
  <!-- 搜索容器 -->
  <div class="search-container">
    <!-- 输入框绑定到 searchQuery 数据属性 -->
    <input type="text" v-model="searchQuery" placeholder="输入搜索内容..." />
    <!-- 搜索按钮触发 search 方法 -->
    <button @click="search">搜索</button>
    <!-- 如果正在加载数据，则显示加载中提示 -->
    <div v-if="loading" class="loading">加载中...</div>
    <!-- 如果数据加载完成，则显示结果 -->
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

export default {
  data() {
    return {
      searchQuery: '', // 用户输入的搜索词
      results: [], // 存储搜索结果的数据数组
      loading: false, // 加载状态标志
      currentPage: 1, // 当前页面编号
      pageSize: 4, // 每页显示的结果数量
      totalPages: 1 // 总页数
    };
  },
  methods: {
    // 发起搜索请求的方法
    async search() {
      this.loading = true; // 设置加载状态为true
      try {
        // 发送GET请求到后端API获取搜索结果
        const response = await axios.get('http://127.0.0.1:8000/essearch/search/', {
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
      } finally {
        this.loading = false; // 无论成功或失败，最终都结束加载状态
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
<style>
.search-container {
  margin: 50px auto; /* 容器居中 */
  width: 600px; /* 固定宽度 */
  text-align: center; /* 文本居中 */
}

input {
  padding: 10px; /* 内边距 */
  width: 70%; /* 宽度占70% */
  margin-right: 10px; /* 右外边距 */
}

button {
  padding: 10px 20px; /* 内边距 */
  background-color: #007bff; /* 背景颜色 */
  color: white; /* 文字颜色 */
  border: none; /* 移除边框 */
  cursor: pointer; /* 鼠标悬停时指针变为手型 */
  margin: 5px; /* 外边距 */
}

button:hover {
  background-color: #0056b3; /* 鼠标悬停时背景颜色变化 */
}

button:disabled {
  background-color: #cccccc; /* 按钮禁用时背景颜色 */
  cursor: not-allowed; /* 鼠标悬停时指针变为禁止符号 */
}

.loading {
  margin-top: 20px; /* 上方外边距 */
  font-size: 18px; /* 字体大小 */
  color: #6c757d; /* 字体颜色 */
}

.result-item {
  border: 1px solid #ccc; /* 边框 */
  padding: 10px; /* 内边距 */
  margin: 10px 0; /* 上下外边距 */
  border-radius: 5px; /* 圆角 */
  background-color: #f8f9fa; /* 背景颜色 */
}

.result-item h3 {
  margin: 0; /* 去除默认上下外边距 */
  font-size: 18px; /* 字体大小 */
}

.result-item p {
  margin: 5px 0 0; /* 上方外边距 */
  font-size: 14px; /* 字体大小 */
  color: #6c757d; /* 字体颜色 */
}

.pagination {
  margin-top: 20px; /* 上方外边距 */
}
</style>