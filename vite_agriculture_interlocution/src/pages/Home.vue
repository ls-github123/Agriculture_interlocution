<template>
  <div class="homepage">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="logo">
        <img :src="`${blobConfig.baseBlobUrl}/core-img/logo.png`" alt="FARMTECH Logo">
      </div>
      <ul class="nav-links">
        <li><a href="#">首页</a></li>
        <li><router-link to="/hme">服务</router-link></li>
        <li><a href="#">产品</a></li>
        <li><a href="#">农业行情</a></li>
        <li><a href="#">联系我们</a></li>
      </ul>
      <div class="icons">
        <router-link to="/SearchData">
          <i class="fas fa-search"></i>
        </router-link>
        <i class="fas fa-shopping-cart"></i>

        <!-- 用户登录图标或已登录头像图标 -->
        <el-dropdown v-if="userInfo" trigger="hover" placement="bottom">
          <span class="el-dropdown-link">
            <img :src="userInfo.picture" class="user-avatar" alt="用户头像" />
          </span>
          <template #dropdown>
            <el-card>
              <div class="user-info">
                <img :src="userInfo.picture" class="avatar-large" alt="用户头像" />
                <p><strong>用户名：</strong> {{ userInfo.username }}</p>
                <p><strong>手机号：</strong> {{ userInfo.phone_number }}</p>
                <p><strong>实名状态：</strong> {{ userInfo.is_verified ? '已认证' : '未认证' }}</p>
                <el-button type="danger" size="small" @click="logout">登出</el-button>
              </div>
            </el-card>
          </template>
        </el-dropdown>
        <el-button v-else type="primary" @click="login">登录</el-button>
      </div>
    </nav>
    <section class="hero" :style="{ backgroundImage: `url(${currentImage})` }">
      <div class="hero-content">
        <h1>农业的未来从这里开始</h1>
        <p>
          了解我们的创新解决方案, 如何从尖端到可持续的改变农业发展。
          我们将为未来农业铺平道路。
        </p>
        <button class="cta-button" @click="navigateToPage(0)">了解更多</button>
      </div>
    </section>
    <section>
      <img :src="d2" alt="展示图片" style="width: 90%; height: auto; margin-top: 100px;margin-bottom: 30px;"/>
      <ul class="HAE-image-list">
        <li v-for="(image, index) in d2_1" :key="index" class="image-item" @click="navigateToPage(index)">
          <img :src="image" alt="展示图片" />
          <p>{{ getText(index) }}</p>
        </li>
      </ul>
    </section>
    <!-- 引入 Footer组件 -->
    <Footer />
  </div>
</template>

<script setup>
// 引入 Vue 组合式 API 函数
import { ref, onMounted, onUnmounted, computed } from 'vue';

// 引入 Element Plus 组件
import { ElButton, ElDropdown, ElCard } from 'element-plus';
import 'element-plus/dist/index.css';

//引入封装的认证逻辑
import { useAuth } from '../composables/useAuth';
import Footer from '../components/Footer.vue';
import blobConfig from '../config/blobConfig';// 引入容器存储资源

// 使用认证逻辑
const { userInfo, login, logout, init } = useAuth();

// 初始化认证状态
onMounted(() => {
  init(); // 初始化认证状态
});

// 图片资源配置
const images = [
  `${blobConfig.baseBlobUrl}/bg-img/1.jpg`,
  `${blobConfig.baseBlobUrl}/bg-img/3.jpg`,
  `${blobConfig.baseBlobUrl}/bg-img/6.jpg`,
  `${blobConfig.baseBlobUrl}/bg-img/7.jpg`,
  `${blobConfig.baseBlobUrl}/bg-img/8.jpg`,
];
const d2 = `${blobConfig.baseBlobUrl}/bg-img/2.jpg`;
const d2_1 = [
  `${blobConfig.baseBlobUrl}/gif/digger.gif`,
  `${blobConfig.baseBlobUrl}/gif/windmill.gif`,
  `${blobConfig.baseBlobUrl}/gif/cereals.gif`,
  `${blobConfig.baseBlobUrl}/gif/tractor.gif`,
  `${blobConfig.baseBlobUrl}/gif/discuss.gif`,
];

// 定义当前图片索引和轮播定时器
const currentIndex = ref(0);
const interval = ref(null);

// 计算属性，获取当前要显示的图片
const currentImage = computed(() => images[currentIndex.value]);

// 获取文本描述
const getText = (index) => {
  const texts = ['最佳服务', '农场管理', '100%天然', '农用设备', '社区讨论'];
  return texts[index];
};

const navigateToPage = (index) => {
  const pages = ['/ProductPage', '/farm-experience', '/ProductPage', '/agricultural-equipment', '/organic-food'];
  window.location.href = pages[index];
};

// 定义图片切换函数
const nextImage = () => {
  currentIndex.value = (currentIndex.value + 1) % images.length;
};

const prevImage = () => {
  currentIndex.value = (currentIndex.value - 1 + images.length) % images.length;
};

onMounted(() => {
  interval.value = setInterval(nextImage, 3000); // 每3秒切换一次图片
});

onUnmounted(() => {
  clearInterval(interval.value); // 清理定时器
});
</script>
  
<style scoped>
/* Navbar Styles */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #7ac142;
}

.logo span {
  color: #000;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1rem;
}

.nav-links a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
}

.icons {
  font-size: 1.2rem;
  color: #333;
  display: flex;
  gap: 1rem;
}

/* Hero Section Styles */
.hero {
  background-image: url('https://example.com/tractor.jpg');
  background-size: cover;
  background-position: center;
  padding: 6rem 2rem;
  color: #ffffff;
  text-align: center;
  position: relative;
}

.hero::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 600px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.hero p {
  font-size: 1rem;
  margin-bottom: 1.5rem;
}

.cta-button {
  background-color: #7ac142;
  color: #fff;
  padding: 0.8rem 2rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.cta-button:hover {
  background-color: #5a9b32;
}


.social-icons {
  display: flex;
  gap: 0.5rem;
}

.social-icons i {
  font-size: 1.2rem;
  cursor: pointer;
  transition: color 0.3s;
}

.social-icons i:hover {
  color: #7ac142;
}



/* 
<!-- Hero Area End -->里面的图标样式
image-item  HAE-image-list  HAE-image-list img
image-item:hover img
*/
.HAE-image-list {
list-style-type: none; /* 移除列表项符号 */
padding: 0; /* 移除默认内边距 */
display: flex; /* 使用 Flexbox 布局 */
justify-content: space-around; /* 横向均匀分布列表项 */
}

.HAE-image-list img {
width: 50px; /* 设置图片宽度 */
height: auto; /* 保持图片比例 */
transition: opacity 0.3s; /* 添加透明度过渡效果 */
}

.image-item {
text-align: center; /* 居中文本 */
margin: 10px; /* 列表项之间的间距 */
cursor: pointer; /* 更改鼠标指针为手形 */
transition: transform 0.3s, box-shadow 0.3s; /* 添加过渡效果 */
}


.image-item:hover img {
opacity: 0.7; /* 图片透明度变化 */
}



/*  */
.FBAE-about-section {
display: flex;
align-items: center;
justify-content: space-between;
padding: 20px;
background-color: #f8f9fa; /* 可以根据实际情况调整背景颜色 */
border-radius: 8px; /* 圆角效果，可选 */
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 阴影效果，可选 */
}

.FBAE-text-content, .image-content {
flex: 1;
padding: 10px;
}

.FBAE-text-content h1 {
font-size: 2em;
color: #333;
}

.FBAE-text-content p {
font-size: 1em;
color: #666;
}

.image-content img {
max-width: 100%;
height: auto;
display: block;
}

</style>
<style scoped>
/* Navbar Styles */
.navbar {
display: flex;
justify-content: space-between;
align-items: center;
padding: 1rem 2rem;
background-color: #ffffff;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.logo {
font-size: 1.5rem;
font-weight: bold;
color: #7ac142;
}

.logo span {
color: #000;
}

.nav-links {
list-style: none;
display: flex;
gap: 1rem;
}

.nav-links a {
text-decoration: none;
color: #333;
font-weight: 500;
}

.icons {
font-size: 1.2rem;
color: #333;
display: flex;
gap: 1rem;
}

/* Hero Section Styles */
.hero {
background-image: url('https://example.com/tractor.jpg');
background-size: cover;
background-position: center;
padding: 6rem 2rem;
color: #ffffff;
text-align: center;
position: relative;
}

.hero::before {
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.5);
z-index: 1;
}

.hero-content {
position: relative;
z-index: 2;
max-width: 600px;
margin: 0 auto;
}

.hero h1 {
font-size: 2.5rem;
margin-bottom: 1rem;
}

.hero p {
font-size: 1rem;
margin-bottom: 1.5rem;
}

.cta-button {
background-color: #7ac142;
color: #fff;
padding: 0.8rem 2rem;
border: none;
border-radius: 4px;
font-size: 1rem;
cursor: pointer;
transition: background-color 0.3s;
}

.cta-button:hover {
background-color: #5a9b32;
}


.social-icons {
display: flex;
gap: 0.5rem;
}

.social-icons i {
font-size: 1.2rem;
cursor: pointer;
transition: color 0.3s;
}

.social-icons i:hover {
color: #7ac142;
}

.user-avatar {
width: 40px;
height: 40px;
border-radius: 50%;
cursor: pointer;
}

.avatar-large {
width: 80px;
height: 80px;
border-radius: 50%;
margin-bottom: 1rem;
}

.user-info {
text-align: center;
}

.HAE-image-list {
  list-style-type: none; /* 移除列表项符号 */
  padding: 0; /* 移除默认内边距 */
  display: flex; /* 使用 Flexbox 布局 */
  justify-content: space-around; /* 横向均匀分布列表项 */
}

.HAE-image-list img {
  width: 50px; /* 设置图片宽度 */
  height: auto; /* 保持图片比例 */
  transition: opacity 0.3s; /* 添加透明度过渡效果 */
}

.image-item {
  text-align: center; /* 居中文本 */
  margin: 10px; /* 列表项之间的间距 */
  cursor: pointer; /* 更改鼠标指针为手形 */
  transition: transform 0.3s, box-shadow 0.3s; /* 添加过渡效果 */
}


.image-item:hover img {
  opacity: 0.7; /* 图片透明度变化 */
}



/*  */
.FBAE-about-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #f8f9fa; /* 可以根据实际情况调整背景颜色 */
  border-radius: 8px; /* 圆角效果，可选 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 阴影效果，可选 */
}

.FBAE-text-content, .image-content {
  flex: 1;
  padding: 10px;
}

.FBAE-text-content h1 {
  font-size: 2em;
  color: #333;
}

.FBAE-text-content p {
  font-size: 1em;
  color: #666;
}

.image-content img {
  max-width: 100%;
  height: auto;
  display: block;
}
</style>  
