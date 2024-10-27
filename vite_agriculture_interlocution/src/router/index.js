import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MessagesView from '../views/MessagesView.vue';
import ServiceNotification from '../views/ServiceNotification.vue';
import WeatherReminder from '../views/WeatherReminder.vue';
import PlantingMessage from '../views/PlantingMessage.vue';
import LikeCommentMessage from '../views/LikeCommentMessage.vue';
import SystemNotification from '../views/SystemNotification.vue';


import FeedbackForm from '../views/FeedbackForm.vue'; // 引入 FeedbackForm 组件
import MessageDetail from '../views/MessageDetail.vue';


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
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
  {
    path: '/service-notification',
    name: 'service-notification',
    component: ServiceNotification,
  },
  {
    path: '/weather-reminder',
    name: 'weather-reminder',
    component: WeatherReminder,
  },
  {
    path: '/planting-message',
    name: 'planting-message',
    component: PlantingMessage,
  },
  {
    path: '/like-comment-message',
    name: 'like-comment-message',
    component: LikeCommentMessage,
  },
  {
    path: '/system-notification',
    name: 'system-notification',
    component: SystemNotification,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;