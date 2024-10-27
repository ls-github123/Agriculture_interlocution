<template>
    <div class="dashboard">
      <h2>用户控制面板</h2>
      <pre>{{ accessToken }}</pre>
      <button @click="logout">退出登录</button>
      <p>用户信息:</p>
      <pre>{{ userInfo }}</pre>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </template>
  
<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '../utils/axios';

// 初始化响应数据和错误消息状态
const userInfo = ref('');
const errorMessage = ref('');
const accessToken =  ref(localStorage.getItem('access_token') || '');

// 加载页面时执行的逻辑
onMounted(async () => {
  if (!accessToken.value) {
    // 如果没有本地存储的令牌，则从URL中尝试获取授权码
    const code = new URLSearchParams(window.location.search).get('code');
    if (code) {
      try {
        const response = await apiClient.post('/user/token/', { code });
        userInfo.value = JSON.stringify(response.data.user_info, null, 2);
        accessToken.value = response.data.access_token;
        localStorage.setItem('access_token', response.data.access_token);
        console.log('用户信息已获取并保存.');
      } catch (error) {
        console.error('获取用户信息失败:', error);
      }
    } else {
      errorMessage.value = '未检测到授权码, 请重新登录!';
    }
  } else {
    // 如果本地有令牌, 则使用它获取用户信息
    await fetchUserInfo();
  }
});

// 使用令牌请求用户信息
async function fetchUserInfo(){
  try {
    const response = await apiClient.get('/user/info/', {
      headers: { Authorization: `Bearer ${accessToken.value}` },
    });
    userInfo.value = JSON.stringify(response.data, null, 2);
  } catch (error) {
    console.error('用户信息获取失败:', error);
    errorMessage.value = '用户信息获取失败,请重新登录。';
    localStorage.removeItem('access_token');
  }
}

// 退出登录
function logout() {
  localStorage.removeItem('access_token');
  const logoutUrl = `https://agricultureinterlocution.authing.cn/oidc/session/end` +
                    `?post_logout_redirect_uri=${encodeURIComponent(window.location.origin)}`;
  window.location.href = logoutUrl;
}
</script>

<style scoped>
.dashboard {
  text-align: center;
  margin-top: 50px;
}

pre {
  background-color: #f4f4f4;
  padding: 10px;
  border-radius: 5px;
  white-space: pre-wrap;
  word-wrap: break-word;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>  