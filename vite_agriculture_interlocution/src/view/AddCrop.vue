<template>
    <div class="add-crop-form">
      <h2>添加新作物</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="name">作物名称：</label>
          <input type="text" id="name" v-model="formData.name" required />
        </div>
        <div class="form-group">
          <label for="plantingDate">种植时间：</label>
          <input type="date" id="plantingDate" v-model="formData.plantingDate" required />
        </div>
        <button type="submit">添加作物</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, emit } from 'vue';
  import apiClient from '../utils/axios';
  
  const formData = ref({
    name: '',
    plantingDate: ''
  });
  
  const handleSubmit = async () => {
    try {
      // 发送请求添加新作物
      const response = await apiClient.post('/custom/crops/', formData.value);
      console.log('作物添加成功:', response.data);
      // 触发事件通知父组件刷新作物列表
      emit('cropAdded');
    } catch (error) {
      console.error('添加作物失败:', error);
      alert('添加作物失败，请重试。');
    }
  };
  </script>
  
  <style scoped>
  .add-crop-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-top: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>