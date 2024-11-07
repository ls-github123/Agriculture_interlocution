<template>
  <div class="harvesting-form">
    <!-- 返回上一页按钮 -->
    <button class="back-btn" @click="goBack">← 返回</button>
    <h2>收割服务申请表</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name">姓名：</label>
        <input type="text" id="name" v-model="formData.name" required />
      </div>
      <div class="form-group">
        <label for="phone">电话：</label>
        <input type="tel" id="phone" v-model="formData.phone" required />
      </div>
      <div class="form-group">
        <label for="address">地址：</label>
        <textarea id="address" v-model="formData.address" required></textarea>
      </div>
      <div class="form-group">
        <label for="cropType">作物类型：</label>
        <select id="cropType" v-model="formData.cropType" required>
          <option value="小麦">小麦</option>
          <option value="玉米">玉米</option>
          <option value="大豆">大豆</option>
          <option value="其它">其它</option>
        </select>
      </div>
      <button type="submit">提交申请</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const formData = ref({
  name: '',
  phone: '',
  address: '',
  cropType: ''
});
// 返回上一页
const goBack = () =>{
       window.history.back()};
       const handleSubmit = async () => {
  // 首先检查表单数据是否完整
  if (!formData.value.name || !formData.value.phone || !formData.value.address || !formData.value.cropType) {
    // 如果数据不完整，显示错误提示并阻止表单提交
    alert('请填写完整信息！');
    return; // 阻止后续代码执行
  }

  try {
    // 如果数据完整，继续发送请求
    const response = await axios.post('http://localhost:3000/api/harvesting', formData.value);
    alert('申请成功！');
    console.log(response.data);
  } catch (error) {
    // 如果请求失败，显示错误提示
    console.error('申请失败:', error);
    alert('申请失败，请重试。');
  }
};



</script>

<style scoped>
/* 你可以在这里添加样式 */
.harvesting-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;
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
label {
  display: block;
  margin-bottom: 5px;
}

input, textarea, select {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>