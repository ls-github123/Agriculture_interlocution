<template>
  <div class="homepage">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="logo">
        <img :src="`${blobConfig.baseBlobUrl}/core-img/logo.png`" alt="FARMTECH Logo">
      </div>
      <ul class="nav-links">
        <li><a href="#">首页</a></li>
        <li><a href="#">获取资料</a></li>
        <li><a href="#">服务</a></li>
        <li><a href="#">产品</a></li>
        <li><a href="#">农业行情</a></li>
        <li><a href="#">联系我们</a></li>
      </ul>
      <div class="icons">
        <i class="fas fa-search"></i>
        <i class="fas fa-shopping-cart"></i>

        <!-- 用户登录图标或已登录头像图标 -->
        <el-dropdown v-if="isLoggedIn" trigger="hover" placement="bottom">
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
                <el-button type="danger" size="small" @click="handleLogout">登出</el-button>
              </div>
            </el-card>
          </template>
        </el-dropdown>
        <el-button v-else type="primary" @click="handleLogin">登录</el-button>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1>农业的未来从这里开始</h1>
        <p>
          了解我们的创新解决方案, 如何从尖端到可持续的改变农业发展。
          我们将为未来农业铺平道路。
        </p>
        <button class="cta-button">了解更多</button>
      </div>
    </section>

    <!-- 引入 Footer组件 -->
    <Footer />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { ElButton, ElDropdown, ElCard } from 'element-plus';
import 'element-plus/dist/index.css';
import { redirectToAuthing, getAuthorizationCode, fetchAndStoreTokens, getUserInfo, logoutAndRedirect } from '../utils/authing';
import Footer from '../components/Footer.vue';
import blobConfig from '../config/blobConfig'; // 引入容器存储资源

// 登录状态和用户信息
const isLoggedIn = ref(false);
const userInfo = ref({
  username: '',
  avatar: `${blobConfig.baseBlobUrl}/bg-img/33.jpg`, // 默认头像
  phone: '',
  isVerified: false,
});

// 处理登录逻辑
const handleLogin = () => {
  console.log("Login button clicked");
  redirectToAuthing(); // 跳转到 Authing 登录页面
};

// 处理登出逻辑
const handleLogout = () => {
  logoutAndRedirect(); // 清除登录状态并重定向到首页
};

// 检查 URL 中 是否包含授权码并处理登录回调
onMounted(async () => {
  const code = getAuthorizationCode();
  if (code) {
    try {
      // 使用授权码获取并存储令牌和用户信息
      await fetchAndStoreTokens(code);
      userInfo.value = getUserInfo(); // 获取并设置用户信息
      isLoggedIn.value = true;
      console.log('登录成功，用户已登录:', isLoggedIn.value); // 调试信息
    } catch (error) {
      console.error('登录失败:', error);
      logoutAndRedirect(); // 如果获取令牌失败，登出并重定向
    }
  } else {
    const user = getUserInfo();
    if (user) {
      userInfo.value ={
        username: user.username || '未知用户',
        picture: user.picture || `${blobConfig.baseBlobUrl}/bg-img/33.jpg`,
        phone: user.phone_number || '未提供',
        isVerified: user.isVerified || false,
      };
      isLoggedIn.value = true;
    }
  }
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
</style>  