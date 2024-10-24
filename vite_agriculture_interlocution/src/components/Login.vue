<template>
    <div class="login">
        <h2>P5实训-农业专家问答系统</h2>
        <button @click="login">使用Authing登录</button>
    </div>
</template>

<script setup>
import { redirectToAuthing, fetchAccessToken } from '../utils/authing';
import { useRouter, useRoute } from 'vue-router';
import { onMounted } from 'vue';

const router = useRouter();
const route = useRoute();

const login = () => {
    redirectToAuthing(); // 跳转到Authing登录页
};

// 在回调页解析授权码并请求 access_token
onMounted(async () => {
    const code = route.query.code;
    if (code) {
        try {
            const token = await fetchAccessToken(code);
            localStorage.setItem('access_token', token);
            router.push('/dashboard'); // 跳转到控制面板
        } catch (error) {
            console.error('登录失败:', error);
        }
    }
});
</script>

<style scoped>
.login {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>