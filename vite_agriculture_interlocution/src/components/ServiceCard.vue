<template>
    <div class="service-card" :style="cardStyle" @click="navigateToService">
      <img :src="service.icon" alt="Service Icon" class="service-icon" />
      <h3 class="service-title">{{ service.title }}</h3>
      <p class="service-content" :style="contentStyle">{{ service.content }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      service: {
        type: Object,
        required: true
      }
    },
    computed: {
      cardStyle() {
        return {
          backgroundColor: this.service.backgroundColor,//背景颜色
          backgroundImage: this.service.backgroundImage,//背景图片
          backgroundSize: 'cover',//背景字体格式
          backgroundPosition: 'center',//背景字体位置
          
        };
      },
  
      contentStyle() {
          return {
            color: this.service.contentColor,
            fontSize: this.service.contentFontSize
          };
        }
    },  
    methods: {
      navigateToService() {
        this.$router.push(this.service.to);
      }
    }
  };
  </script>
  
  <style scoped>
  .service-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
    color: #333; /* 文字颜色 */
  }
  
  .service-card:hover {
    transform: scale(1.05);
  }
  
  .service-icon {
    width: 64px;
    height: 64px;
    margin-bottom: 10px;
  }
  
  .service-title {
    font-size: 18px;
    margin: 0 0 10px;
    color: #333;
  }
  
  .service-content {
    font-size: 14px;
    color: #666;
  }
  </style>