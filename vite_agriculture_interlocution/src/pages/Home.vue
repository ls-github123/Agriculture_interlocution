<template>
  <div class="homepage">
    <nav class="navbar">
      <div class="logo">FARM<span>TECH</span></div>
      <ul class="nav-links">
        <li><a href="#">首页</a></li>
        <li><router-link to="/SearchData">科普</router-link></li>
        <li><a href="#">服务</a></li>
        <li><a href="#">我们的产品</a></li>
        <li><a href="#">农业行情</a></li>
        <li><a href="#">联系我们</a></li>
        <li><router-link to="/login">登录</router-link></li>
      </ul>
      <div class="icons">
        <i class="fas fa-search"></i>
        <i class="fas fa-shopping-cart"></i>
      </div>
    </nav>
    <section class="hero" :style="{ backgroundImage: `url(${currentImage})` }">
      <div class="hero-content">
        <h1>The Future of Agriculture Starts Here</h1>
        <p>
          Discover how our innovative solutions are transforming the agriculture industry. 
          From cutting-edge technology to sustainable practices, we're paving the way for the future.
        </p>
        <button class="cta-button" @click="navigateToPage(0)">Learn More</button>
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
    <section class="FBAE-about-section">
      <div class="FBAE-text-content">
        <p>Let Us Tell You Our Story</p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam nunc elit, pretium atlanta urna veloci,
          fermentum malesuada mina. Donec auctor nislec neque sagittis, sit amet dapibus pellentesque donal feugiat.
          Nulla mollis magna non sanaliquet, volutpat do zutum, ultrices consectetur, ultrices at purus.
        </p>
      </div>
      <div class="image-content">
        <img src="#" alt="描述性文字" />
      </div>
    </section>
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-section about">
          <h2>About Us</h2>
          <p>FARMTECH is dedicated to advancing agriculture through innovative solutions and sustainable practices.</p>
        </div>
        <div class="footer-section links">
          <h2>Quick Links</h2>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Products</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </div>
        <div class="footer-section contact">
          <h2>Contact Us</h2>
          <p><i class="fas fa-phone"></i> +123 456 789</p>
          <p><i class="fas fa-envelope"></i> info@farmtech.com</p>
          <p><i class="fas fa-map-marker-alt"></i> 123 Agriculture St., City, Country</p>
        </div>
        <div class="footer-section social">
          <h2>Follow Us</h2>
          <div class="social-icons">
            <i class="fab fa-facebook-f"></i>
            <i class="fab fa-twitter"></i>
            <i class="fab fa-instagram"></i>
            <i class="fab fa-linkedin-in"></i>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2024 FARMTECH | Designed by YourCompany</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import blobConfig from '../config/blobConfig';

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
const currentIndex = ref(0);
const interval = ref(null);

const currentImage = computed(() => images[currentIndex.value]);

const getText = (index) => {
  const texts = ['最佳服务', '农场管理', '100%天然', '农用设备', '社区讨论'];
  return texts[index];
};

const navigateToPage = (index) => {
  const pages = ['/service', '/farm-experience', '/natural-products', '/agricultural-equipment', '/organic-food'];
  window.location.href = pages[index];
};

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
  
  /* Footer Styles */
  .footer {
    background-color: #333;
    color: #ffffff;
    padding: 2rem 1rem;
  }
  
  .footer-content {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }
  
  .footer-section {
    flex: 1;
    min-width: 200px;
    margin-bottom: 1rem;
  }
  
  .footer-section h2 {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
  }
  
  .footer-section p,
  .footer-section ul,
  .footer-section li {
    font-size: 0.9rem;
  }
  
  .footer-section ul {
    list-style: none;
    padding: 0;
  }
  
  .footer-section li {
    margin-bottom: 0.3rem;
  }
  
  .footer-section a {
    color: #ffffff;
    text-decoration: none;
    transition: color 0.3s;
  }
  
  .footer-section a:hover {
    color: #7ac142;
  }
  
  .footer-bottom {
    text-align: center;
    font-size: 0.8rem;
    padding-top: 1rem;
    border-top: 1px solid #555;
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