<template>
    <div class="login">
        <h2>P5实训-农业专家问答系统</h2>
        <button @click="login">使用 Authing 登录</button>
    </div>
</template>

<script setup>
import { redirectToAuthing } from '../utils/authing'; // 导入封装的登录逻辑

// 调用封装的登录函数
const login = () => {
    console.log('开始跳转到 Authing 登录页');
    redirectToAuthing(); // 调用封装的跳转函数
};
</script>

<style scoped>
.login {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>