import { createRouter, createWebHistory } from 'vue-router';





// 懒加载组件
const Home = () => import('../pages/Home.vue');
const SearchData = () => import('../components/SearchData.vue');

const ProductPage = () => import('../components/ProductPage.vue');
const CartPage = () => import('../components/CartPage.vue');



const routes = [


    { path: '/cart', component: CartPage },
    { path: '/ProductPage', component: ProductPage },


    { path: '/', name: 'Home', component: Home },
    { path: '/SearchData', component: SearchData },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;