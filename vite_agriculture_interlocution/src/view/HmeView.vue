<template>
    <div class="home-page">
      <div class="content">
        <h1>欢迎来到智农服务</h1>
        <p>为您提供最优质的农业服务和技术支持。</p>
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
    background-image: url('../../public/images/backphool.png'); /* 替换为你的背景图片路径 */
    background-size: cover;
    background-position: center;
    padding: 20px;
    color: #ffffff; /* 文字颜色调整为白色，以便在深色背景上更清晰 */
  }
  
  .content {
    text-align: center;
    background-color: rgba(255, 255, 255, 0.8); /* 半透明背景色 */
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 40px;
    max-width: 500px;
    width: 100%;
    transition: transform 0.3s ease-in-out;
  }
  
  .content:hover {
    transform: scale(1.05);
  }
  
  h1 {
    font-size: 2.5em;
    color: #333333;
    margin-bottom: 20px;
  }
  
  p {
    font-size: 1.2em;
    color: #666666;
    margin-bottom: 30px;
  }
  
  .button {
    display: inline-block;
    text-align: center;
    background-color: #2196F3;
    color: #ffffff;
    border-radius: 6px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 12px 24px;
    font-size: 1.1em;
    text-decoration: none;
    transition: background-color 0.3s ease-in-out, transform 0.3s ease-in-out;
  }
  
  .button:hover {
    background-color: #0D47A1;
    transform: translateY(-2px);
  }
  </style>