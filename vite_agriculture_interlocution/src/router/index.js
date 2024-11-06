import { createRouter, createWebHistory } from 'vue-router';





// 懒加载组件
const Home = () => import('../pages/Home.vue');
const SearchData = () => import('../components/SearchData.vue');

const ProductPage = () => import('../components/ProductPage.vue');
const CartPage = () => import('../components/CartPage.vue');

const OrderListPage = () => import('../components/OrderListPage.vue');
const OrderDetailPage = () => import('../components/OrderDetailPage.vue');

const routes = [
    { path: '/orders', name: 'OrderListPage',component: OrderListPage },
    { path: '/orders/:id', name: 'OrderDetailPage',component: OrderDetailPage ,props: true },// 允许将路由参数传递给组件作为 props

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