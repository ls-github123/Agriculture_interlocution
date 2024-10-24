<template>
    <div class="dashboard">
      <h2>用户控制面板</h2>
      <button @click="logout">退出登录</button>
      <pre>{{ userInfo }}</pre>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  // 存储用户信息
  const userInfo = ref(null);
  
  // 获取用户信息
  const fetchUserInfo = async () => {
    try {
      const token = localStorage.getItem('access_token');
      const response = await axios.get(
        'https://agricultureinterlocution.authing.cn/oidc/me',
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      userInfo.value = response.data; // 保存用户信息
    } catch (error) {
      console.error('获取用户信息失败:', error);
    }
  };
  
  // Authing 配置
  const AUTHING_CONFIG = {
    appId: '671a02c6ef4cdd625a133fcd', // 替换为你的真实 App ID
    logoutEndpoint: 'https://agricultureinterlocution.authing.cn/oidc/session/end', // 登出端点
    postLogoutRedirectUri: 'http://localhost:5173/', // 登出后的重定向地址
  };
  
  // 退出登录，清除本地 access_token，并重定向到 Authing 登出端点
  const logout = () => {
    localStorage.removeItem('access_token'); // 清除本地存储的 access_token
  
    // 构造 Authing 登出 URL
    const logoutUrl = `${AUTHING_CONFIG.logoutEndpoint}` +
      `?client_id=${AUTHING_CONFIG.appId}` +
      `&post_logout_redirect_uri=${encodeURIComponent(AUTHING_CONFIG.postLogoutRedirectUri)}`;
  
    // 重定向到 Authing 托管的登出页
    window.location.href = logoutUrl;
  };
  
  // 在组件挂载时调用 fetchUserInfo
  onMounted(fetchUserInfo);
  </script>
  
  <style scoped>
  .dashboard {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  </style>  