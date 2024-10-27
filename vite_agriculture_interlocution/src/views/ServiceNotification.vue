<template>
  <div class="message-detail">
    <h1>服务通知</h1>
    <p>这里是服务通知的详细内容。</p>
  </div>
</template>

<script>
export default {
  name: 'ServiceNotification',
};
</script>

<style scoped>
.message-detail {
  padding: 20px;
  text-align: center;
  background-color: #f0f2f5;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

h1 {
  font-size: 2em;
  margin-bottom: 20px;
}

p {
  font-size: 16px;
  max-width: 600px;
  text-align: left;
  line-height: 1.6;
}
</style>