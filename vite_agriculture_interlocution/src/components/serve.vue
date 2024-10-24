<template>
  <div>
    <header>
      <img src="map-pic.png" alt="Header Image">
      <div class="header-buttons">
        <button @click="showMore">更多中心 &gt;</button>
      </div>
    </header>

    <main>
      <section id="location-section">
        <h1>北京市东城区东华门</h1>
        <p>距您 31.01公里</p>
        <div class="buttons">
          <button @click="navigate">导航</button>
          <button @click="call">电话</button>
        </div>
      </section>

      <section id="services-section">
        <div class="service-button">
          <i class="fas fa-truck"></i>
          <button>找农机</button>
        </div>
        <div class="service-button">
          <i class="fas fa-search"></i>
          <button>查找中心</button>
        </div>
      </section>

      <section id="promotion-section">
        <img src="promotion-image.jpg" alt="Promotion Image">
      </section>

      <section id="introduction-section">
        <h1>服务介绍</h1>
        <article>
          <img src="service-image.jpg" alt="Service Image">
        </article>
      </section>
    </main>

    <footer>
      <nav>
        <ul>
          <li><a href="#">首页</a></li>
          <li><a href="#">农场</a></li>
          <li><a href="#">消息</a></li>
          <li><a href="#">MAP服务</a></li>
          <li><a href="#">我的</a></li>
        </ul>
      </nav>
    </footer>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'GuangYuanServiceCenter',
  setup() {
    const showMore = () => {
      console.log('显示更多服务中心');
    };

    const navigate = () => {
      window.location.href = "https://amap.com/";
    };

    const call = () => {
      window.location.href = "tel:186-6714-1302";
    };

    return {
      showMore,
      navigate,
      call,
    };
  }
});
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
}

header img {
  width: 100%;
}

.header-buttons button {
  background-color: transparent;
  border: none;
  color: #007bff;
  cursor: pointer;
  font-size: 1rem;
  margin-top: 1rem;
}

.buttons button {
  background-color: #007bff;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 1rem;
  margin-right: 1rem;
  padding: 0.5rem 1rem;
  border-radius: 5px;
}

.service-button {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.service-button i {
  font-size: 2rem;
  color: #007bff;
  margin-right: 0.5rem;
}

.service-button button {
  background-color: transparent;
  border: none;
  color: #007bff;
  font-size: 1.5rem;
  cursor: pointer;
}

footer nav ul {
  list-style: none;
  text-align: center;
  padding: 1rem 0;
}

footer nav ul li {
  display: inline-block;
  margin: 0 1rem;
}

footer nav ul li a {
  text-decoration: none;
  color: black;
  font-size: 1rem;
}

@media (max-width: 768px) {
  .service-button {
    flex-direction: column;
    align-items: flex-start;
  }

  .service-button i {
    margin-bottom: 0.5rem;
  }
}
</style>
