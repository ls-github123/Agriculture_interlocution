<template>
  <div class="home-page">
    <div class="content">
      <h1>欢迎来到主页</h1>
      <van-button type="primary" to="/messages">消息</van-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
};
</script>

<style scoped>
.home-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f2f5;
  padding: 20px;
}

.content {
  text-align: center;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  max-width: 600px;
  width: 100%;
}

h1 {
  font-size: 2em;
  margin-bottom: 20px;
}

.van-button {
  width: 80%;
  font-size: 16px;
  margin-top: 20px;
}
</style>