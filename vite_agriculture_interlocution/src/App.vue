<template>
  <div id="app">
    <router-view />  <!-- 路由视图用于渲染当前匹配的页面组件 -->
  </div>
</template>

<script setup>
// App.vue 不需要逻辑部分，只作为布局组件
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased; /* 对于 WebKit 内核的浏览器进行字体平滑 */
  -moz-osx-font-smoothing: grayscale; /* 对于 MacOS 系统下的 Firefox 进行字体平滑 */
  text-align: center;
  color: #2c3e50; /* 文本颜色 */
  margin-top: 60px;
}

/* 可以添加更多的样式规则来美化应用程序 */
</style>