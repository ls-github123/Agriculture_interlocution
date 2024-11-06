<template>
    <div class="home-page">
      <div class="content">
        <h1>欢迎来到智农服务</h1>
        <router-link to="/service" class="button">进入</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HmeView',
  };
  </script>
  
  <style scoped>
  .home-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #e3e9e5;
    padding: 20px;
  }
  
  .content {
    text-align: center;
    background-color: rgb(49, 18, 227);
    border-radius: 6px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 30px;
    max-width: 500px;
    width: 80%;
  }
  .button{
    text-align: center;
    background-color: rgb(227, 18, 18);
    border-radius: 6px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 5px;
    max-width: 50px;
    width: 80%;
  }
  h1 {
    font-size: 2em;
    margin-bottom: 20px;
  }
  
  .van-button {
    width: 80%;
    font-size: 16px;
    margin-top: 20px;
  }
  </style>