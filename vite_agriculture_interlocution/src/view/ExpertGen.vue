<template>
    <div class="container">
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
  
  // AI生成的回答
  const aiMsg = ref('');
  
  // 发送请求
  function fnPostIssueInfo() {
    axios.post('http://127.0.0.1:8000/api/genename/?species=', issue_info.species)
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