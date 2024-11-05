import { createRouter, createWebHistory } from 'vue-router';

// 懒加载组件
const Home = () => import('../pages/Home.vue');
const SearchData = () => import('../components/SearchData.vue');

const routes = [
    { path: '/home', name: 'Home', component: Home },
    { path: '/SearchData', component: SearchData },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;