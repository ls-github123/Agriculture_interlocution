import { createRouter, createWebHistory } from 'vue-router';
import Serve from '../components/serve.vue'; // 注意首字母大写
import Agricultural from '../components/Agricultural.vue';

// 可以根据需要导入更多的组件
// import AnotherComponent from '../components/AnotherComponent.vue';

const routes = [
  {
    path: '/',
    name: 'agricultural', // 给路由命名，方便引用
    component: Agricultural,
  },
  {
    path: '/serve',
    name: 'Serve', // 给路由命名，方便引用
    component: Serve,
  },
  // 可以在这里添加更多的路由
  // {
  //   path: '/another',
  //   name: 'Another',
  //   component: AnotherComponent,
  // },
  // 如果需要重定向
  // {
  //   path: '/old-path',
  //   redirect: to => {
  //     return { name: 'Serve' }
  //   }
  // },
  // 404 Not Found 路由
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../components/NotFound.vue'), // 懒加载组件
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes, // 这里不需要逗号
});

export default router;
