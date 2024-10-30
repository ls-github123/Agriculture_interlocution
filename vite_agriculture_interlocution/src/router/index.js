import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MessagesView from '../views/0-MessagesView.vue';


import FeedbackForm from '../views/0-FeedbackForm.vue'; // 引入 FeedbackForm 组件
import MessageDetail from '../views/2-MessageDetail.vue';

import GoPage from '../views/GoPage.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/go/:type',
    name: 'GoPage',
    component: GoPage,
    props: true  // 传递路由参数作为组件的props
  },
  {
    path: '/message-detail/:messageId',
    name: 'MessageDetail',
    component: MessageDetail,
  },
  {
    path: '/feedback-form',
    name: 'feedback-form',
    component: FeedbackForm,
  },
  {
    path: '/messages',
    name: 'messages',
    component: MessagesView,
  },

];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;