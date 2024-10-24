import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import Dashboard from '../components/Dashboard.vue';

const routes = [
    { path: '/', component: Login },
    { path: '/dashboard', component: Dashboard },
    { path: '/callback', component: Login }, //回调页
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;