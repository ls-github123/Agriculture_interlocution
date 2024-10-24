import { createRouter, createWebHistory } from 'vue-router';
import serve from '../components/serve.vue';

const routes = [
    { path: '/', component: serve },
    {path:''},
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;