import { createRouter, createWebHistory } from 'vue-router';
import Home from '../pages/Home.vue';
import Login from '../components/Login.vue';
import Dashboard from '../components/Dashboard.vue';
import SearchData from '../components/SearchData.vue';

const routes = [
    { path: '/home', name: 'Home', component: Home },
    { path: '/SearchData', component: SearchData },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

