import { createRouter, createWebHistory } from 'vue-router';
import Home from '../pages/Home.vue';
import Login from '../components/Login.vue';
import Dashboard from '../components/Dashboard.vue';

const routes = [
    { path: '/', component: Home },
    { path: '/login', component: Login }, // 添加login路由
    { path: '/dashboard', component: Dashboard },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;