// 应用入口文件
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { getAuthorizationCode, fetchAndStoreTokens } from './utils/authing';
import '@fortawesome/fontawesome-free/css/all.css'; // 引入 FontAwesome 样式

// createApp(App).use(router).mount('#app');
const app = createApp(App);

// 检查 URL 中是否包含授权码
const code = getAuthorizationCode();
if (code) {
    // 使用授权码获取令牌并存储
    fetchAndStoreTokens(code).then(() => {
        // 移除URL中的授权码参数, 保持 URL 简洁
        window.history.replaceState({}, document.title, window.location.pathname);
        app.use(router).mount('#app');
    }).catch((error) => {
        console.error('登录失败:', error);
        app.use(router).mount('#app');
    });
} else {
    // 正常启动应用
    app.use(router).mount('#app');
}