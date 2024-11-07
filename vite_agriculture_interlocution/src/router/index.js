import { createRouter, createWebHistory } from 'vue-router';

// 懒加载组件
const Home = () => import('../pages/Home.vue');
const SearchData = () => import('../components/SearchData.vue');

// 引入认证相关函数
import { getAuthorizationCode, fetchAndStoreTokens, isAuthenticated } from '../utils/authing';

// 定义路由
const routes = [
    { path: '/', name: 'Home', component: Home },//主页
    { path: '/SearchData', component: SearchData },//搜索
    {path:'/hme',component:HmeView},//服务
    {path:'/service',component:Service},//选择服务
    {path:'/expert',name:'expertgen',component:ExpertGen},//专家
    {path:'/harvesting',name:'harvest',component:HarvestingFrom},//收割服务
    {path:'/irrigation',component:IrrigationFrom}
];

// 创建路由实例
const router = createRouter({
    history: createWebHistory(),
    routes,
});

// 清除 URL 中的授权码和状态参数，带延时机制
function clearUrlParams() {
    setTimeout(() => {
        const url = new URL(window.location.href);
        url.searchParams.delete('code');
        url.searchParams.delete('state');
        window.history.pushState(null, '', url.toString()); // 强制更新 URL
        window.history.replaceState(null, '', url.toString());
        console.log('URL 中的 code 和 state 参数已清除');
    }, 100); // 延时以确保存储操作完成
}

// 检查是否有授权码并获取令牌
async function handleAuthorizationCode(next) {
    const code = getAuthorizationCode();
    if (code) {
        try {
            await fetchAndStoreTokens(code);
            clearUrlParams();
            next(); // 成功后导航
        } catch (error) {
            console.error('获取令牌失败:', error);
            next('/home'); // 失败时重定向到主页
        }
        return true; // 表示已处理授权码
    }
    return false; // 未发现授权码
}

// 添加全局前置守卫
router.beforeEach(async (to, from, next) => {
    try {
        // 检查并处理授权码
        const handled = await handleAuthorizationCode(next);
        if (handled) return;

        // 检查目标路由是否需要认证
        if (to.meta.requiresAuth && !isAuthenticated()) {
            console.warn(`访问受限页面: ${to.path}，用户未认证，重定向到主页`);
            next('/home');
        } else {
            next(); // 用户已认证或不需要认证，继续导航
        }
    } catch (error) {
        console.error('路由守卫中发生错误:', error);
        next('/home'); // 出现错误时重定向到主页
    }
});

export default router;

