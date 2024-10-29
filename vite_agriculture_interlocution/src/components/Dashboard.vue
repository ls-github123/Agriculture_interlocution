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
import { getAuthorizationCode, fetchAndStoreTokens, getAccessToken, isTokenExpired, refreshAccessToken, logoutAndRedirect } from '../utils/authing';
import apiClient from '../utils/axios';

const userInfo = ref(null);
const errorMessage = ref('');
const accessToken = ref(null);
const loading = ref(false); // 添加 loading 状态

// onMounted -- Vue 3 中的 生命周期钩子
// 在组件第一次挂载时执行
onMounted(async () => {
  try {
    const code = getAuthorizationCode(); // URL 中提取授权码 code
    loading.value = true; // 开始加载

    if (code) {
      await fetchAndStoreTokens(code); // 使用授权码code从后端获取令牌
      // 从内存或 sessionStorage 中获取 access_token
    } else if (!getAccessToken() || isTokenExpired(getAccessToken())) {
      await refreshAccessToken(); // 使用 refresh_token 向服务器请求新的 access_token
    } else {
      await fetchUserInfo(); // 使用有效令牌请求用户信息
    }

    await fetchUserInfo(); // 获取用户信息
  } catch (error) {
    errorMessage.value = error.message || '操作失败，请重新登录';
    console.error(error);
  } finally {
    loading.value = false; // 加载结束
  }
});

// 获取用户信息
async function fetchUserInfo() {
  try {
    const token = getAccessToken();
    accessToken.value = token; // 保存 access_token

    const { data } = await apiClient.get('/user/user_info/', {
      headers: { Authorization: `Bearer ${token}` },
    });
    userInfo.value = JSON.stringify(data, null, 2);
  } catch (error) {
    errorMessage.value = '获取用户信息失败, 请重新登录';
    console.error('获取用户信息失败:', error);
  }
}

// 退出登录
function logout() {
  logoutAndRedirect();
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