<template>
    <div class="container">
      <!-- 返回上一页按钮 -->
       <button class="back-btn" @click="goBack">← 返回</button>
      <h2>农事咨询</h2>
      <form @submit.prevent="fnPostIssueInfo">
        <div class="form-group">
          <label for="species">咨询：</label>
          <input type="text" id="species" v-model="issue_info.species" required>
        </div>
        
        <button type="submit" class="btn">生成</button>
      </form>
      <p class="ai-response">{{ aiMsg }}</p>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { reactive, ref } from 'vue';
  
  // 定义姓名信息
  const issue_info = reactive({
    species: '',
    
  });
  // 返回上一页
    const goBack = () =>{
       window.history.back()};
  // AI生成的回答
  const aiMsg = ref('');
  
  // 发送请求
  function fnPostIssueInfo() {
    axios.post('http://127.0.0.1:8000/app/genename/', {species:issue_info.species})
      .then((response) => {
        if (response.data.code === 200) {
          
          aiMsg.value = result.data.aiMessage;
          console.log(result.data);
        }else {
            alert('生成失败，请稍后再试');}
      })
      .catch((err) => {
        console.error('提交失败:', err);
        alert('请稍后再试');
      });
  }
  </script>
  
  <style scoped>
  .container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    text-align: center;
    color: #333;
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
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #555;
  }
  
  input[type="text"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  .btn {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .btn:hover {
    background-color: #0056b3;
  }
  
  .ai-response {
    margin-top: 20px;
    padding: 10px;
    background-color: #eef5ff;
    border-radius: 4px;
    text-align: center;
    color: #333;
  }
  </style>