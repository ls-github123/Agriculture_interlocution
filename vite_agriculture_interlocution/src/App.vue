<template>
  <div id="app">
    <router-view></router-view>  <!-- 路由视图用于渲染当前匹配的页面组件 -->
  </div>
</template>

<script setup>
// App.vue 不需要逻辑部分，只作为布局组件
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
}
</style>
