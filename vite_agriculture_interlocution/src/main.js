import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import '@fortawesome/fontawesome-free/css/all.css'; // 引入 FontAwesome 样式

createApp(App).use(router).mount('#app');