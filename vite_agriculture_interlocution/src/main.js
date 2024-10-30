import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'vant/lib/index.css'; // 引入 Vant 样式
import { Button, Cell, CellGroup, Icon, NavBar,Tab, Tabs, Toast, Tag } from 'vant';

// 引入 Font Awesome
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

// 添加 Font Awesome 图标库
library.add(fas);

const app = createApp(App);

// 使用 Vant 组件
app.use(Button);
app.use(Cell);
app.use(CellGroup);
app.use(Icon);
app.use(NavBar); 
app.use(Tab);
app.use(Tabs);
app.use(Toast);
app.use(Tag);

// 注册 FontAwesomeIcon 组件
app.component('font-awesome-icon', FontAwesomeIcon);

// 使用路由
app.use(router);

// 挂载应用
app.mount('#app');