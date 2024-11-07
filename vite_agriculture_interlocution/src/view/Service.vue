<template>
    <div class="home">
      <el-row :gutter="20">
        <el-col :span="8" v-for="(service, index) in services" :key="index">
          <ServiceCard :service="service" />
        </el-col>
      </el-row>
    </div>
  </template>
  
  <script>
  import ServiceCard from '../components/ServiceCard.vue';
  
  export default {
    components: {
      ServiceCard
    },
    data() {
      return {
        services: [
          {
            icon: '/images/farming.png',
            title: '种植服务',
            content: '提供专业的种植技术服务，包括土壤检测、种子选择等。',
            to: '/services/farming',
            backgroundColor: '#1bed1b', // 背景颜色
            backgroundImage: 'url(/images/irrigatn.png)', // 背景图片
            contentColor: '#333333',//内容颜色
            contentFontSize: '20px',//内容字体大小
          },
          {
            icon: '/images/irrigation.png',
            title: '灌溉服务',
            content: '提供高效的灌溉系统设计和安装服务，确保农作物得到充足的水分。',
            to: '/irrigation',
            backgroundColor: '#f0f8ff', // 背景颜色
            backgroundImage: 'url(images/background.jpg)', // 背景图片
            contentColor: '#333333',//内容颜色
            contentFontSize: '20px',//内容字体大小
          },
          {
            icon: '/images/harvest.png',
            title: '收割服务',
            content: '提供专业的收割服务，确保农作物在最佳时机收获。',
            to: '/harvesting',
            backgroundColor: '#f6fcf6', // 背景颜色
            backgroundImage: 'url(/images/background2.jpg)' ,// 背景图片
            contentColor: '#333333',//内容颜色
            contentFontSize: '20px',//内容字体大小
          },
          {
            icon: '/images/expert.png',
            title: '专家咨询服务',
            content: '提供专业的专家咨询服务，确保用户了解当前作物的生长情况，市场需求以及对未来的规划。',
            to: '/expert',
            backgroundColor: '#f6fcf6', // 背景颜色
            backgroundImage: 'url(/images/background3.jpg)', // 背景图片
            contentColor: '#333333',//内容颜色
            contentFontSize: '20px',//内容字体大小
          },
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .home {
    max-width: 1200px;
    margin: 0 auto;
    padding: 100px;
    background-color: #f6fcf6;
  }
  </style>