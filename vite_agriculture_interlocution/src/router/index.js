import { createRouter, createWebHistory } from 'vue-router';
import Home from '../pages/Home.vue';
import SearchData from '../components/SearchData.vue';

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/SearchData', component: SearchData },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

