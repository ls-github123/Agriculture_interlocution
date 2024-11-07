import { createRouter, createWebHistory } from 'vue-router';
import Home from '../pages/Home.vue';
import SearchData from '../components/SearchData.vue';
import HmeView from '../view/HmeView.vue';
import Service from '../view/Service.vue';
import ExpertGen from '../view/ExpertGen.vue';
import HarvestingFrom from '../view/HarvestingFrom.vue';
import IrrigationFrom from '../view/IrrigationFrom.vue';

const routes = [
    { path: '/', name: 'Home', component: Home },//主页
    { path: '/SearchData', component: SearchData },//搜索
    {path:'/hme',component:HmeView},//服务
    {path:'/service',component:Service},//选择服务
    {path:'/expert',name:'expertgen',component:ExpertGen},//专家
    {path:'/harvesting',name:'harvest',component:HarvestingFrom},//收割服务
    {path:'/irrigation',component:IrrigationFrom}
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

