<template>
    <div>
       <!-- 返回上一页按钮 -->
    <button class="back-btn" @click="goBack">← 返回</button>
      <h2>作物列表</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>作物名称</th>
            <th>种植时间</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="crop in crops" :key="crop.id">
            <td>{{ crop.id }}</td>
            <td>{{ crop.name }}</td>
            <td>{{ crop.plantingDate }}</td>
            <td>
              <button @click="editCrop(crop.id)">编辑</button>
              <button @click="deleteCrop(crop.id)">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
      <AddCrop @cropAdded="fetchCrops" />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import AddCrop from './AddCrop.vue';
  import axios from 'axios';
  import apiClient from '../utils/axios';
  const router = useRouter();
  const crops = ref([]);
  
  const fetchCrops = async () => {
    try {
      const response = await apiClient.get('/api/crops');
      crops.value = response.data;
    } catch (error) {
      console.error('获取作物列表失败:', error);
    }
  };
  
  const deleteCrop = async (id) => {
    try {
      await apiClient.delete(`/api/crops/${id}`);
      await fetchCrops();
    } catch (error) {
      console.error('删除作物失败:', error);
    }
  };
  
  const editCrop = (id) => {
    router.push({ name: 'UpdateCrop', params: { id } });
  };
  
  onMounted(() => {
    fetchCrops();
  });
  </script>
  
  <style scoped>
  /* 通用样式 */
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
  }
  
  /* 容器样式 */
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  .back-btn {
    float: left; /* 让按钮靠左浮动 */  
  padding: 10px 20px; /* 按钮内边距 */
  font-size: 16px; /* 字体大小 */
  color: #fff; /* 字体颜色 */
  background-color: #007bff; /* 背景颜色 */
  border: none; /* 无边框 */
  border-radius: 5px; /* 边框圆角 */
  cursor: pointer; /* 鼠标悬停时显示指针 */
  transition: background-color 0.3s; /* 背景颜色渐变效果 */
}

.back-btn:hover {
  background-color: #0056b3; /* 鼠标悬停时的背景颜色 */
}

.back-btn:active {
  background-color: #004085; /* 按钮被按下时的背景颜色 */
}
  /* 标题样式 */
  h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
  }
  
  /* 表格样式 */
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  th, td {
    padding: 12px;
    text-align: left;
    border: 1px solid #ddd;
  }
  
  th {
    background-color: #f2f2f2;
    font-weight: bold;
    color: #333;
  }
  
  /* 操作按钮样式 */
  button {
    background-color: #4CAF50;
    color: white;
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-right: 5px;
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  button.delete {
    background-color: #f44336;
  }
  
  button.delete:hover {
    background-color: #e53935;
  }
  
  /* 添加作物组件样式 */
  .add-crop {
    margin-top: 20px;
    text-align: center;
  }
  
  .add-crop button {
    background-color: #2196F3;
  }
  
  .add-crop button:hover {
    background-color: #1E88E5;
  }
  </style>