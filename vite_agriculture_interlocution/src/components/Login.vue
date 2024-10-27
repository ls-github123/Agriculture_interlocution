<template>
    <div class="login">
        <h2>P5实训-农业专家问答系统</h2>
        <button @click="login">使用 Authing 登录</button>
    </div>
</template>

<script setup>
const clientId = '671a02c6ef4cdd625a133fcd';
const redirectUri = 'http://localhost:5173/dashboard'

const login = () => {
    const authUrl = 
        `https://agricultureinterlocution.authing.cn/oidc/auth` +
        `?client_id=${clientId}` +
        `&redirect_uri=${encodeURIComponent(redirectUri)}` +
        `&response_type=code` +
        `&scope=openid profile email`;

    console.log("跳转 URL:", authUrl);  // 打印 URL 以便调试
    window.location.href = authUrl;  // 跳转到 Authing 登录页面
};
</script>

<style scoped>
.login {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>