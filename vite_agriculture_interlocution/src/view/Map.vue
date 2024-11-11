<template>
    <div id="app">
      <l-map :zoom="zoom" :center="center" style="height: 100vh; width: 100%;">
        <l-tile-layer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          :attribution="attribution"
        />
        <l-marker
          v-for="farm in farms"
          :key="farm.id"
          :lat-lng="[farm.latitude, farm.longitude]"
        ></l-marker>
      </l-map>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { LMap, LTileLayer, LMarker } from 'vue3-leaflet';
  import axios from 'axios';
  
  export default {
    name: 'App',
    components: {
      LMap,
      LTileLayer,
      LMarker,
    },
    setup() {
      const zoom = ref(6);
      const center = ref([30.67, 104.06]); // 成都坐标，修改为你需要的中心点
      const farms = ref([]);
      const attribution = '© OpenStreetMap contributors';
  
      onMounted(async () => {
        const response = await axios.get('http://localhost:8000/app/farms/');
        farms.value = response.data;
      });
  
      return {
        zoom,
        center,
        farms,
        attribution,
      };
    },
  };
  </script>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  </style>