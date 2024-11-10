<template>
    <div class="planting-service">
      <h1>种植服务管理</h1>
  
      <section>
        <h2>农田管理</h2>
        <form @submit.prevent="manageField">
          <label for="fieldName">农田名称:</label>
          <input type="text" id="fieldName" v-model="fieldName" required />
  
          <label for="fieldSize">农田面积 (亩):</label>
          <input type="number" id="fieldSize" v-model="fieldSize" required />
  
          <button type="submit">管理农田</button>
        </form>
        <p v-if="fieldMessage">{{ fieldMessage }}</p>
      </section>
  
      <section>
        <h2>土壤检测</h2>
        <button @click="testSoil">检测土壤</button>
        <p v-if="soilResult">{{ soilResult }}</p>
      </section>
  
      <section>
        <h2>种子选择</h2>
        <select v-model="selectedSeed">
          <option v-for="seed in seeds" :key="seed.id" :value="seed.name">
            {{ seed.name }}
          </option>
        </select>
        <button @click="selectSeed">选择种子</button>
        <p v-if="selectedSeedMessage">{{ selectedSeedMessage }}</p>
      </section>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    setup() {
      const fieldName = ref('');
      const fieldSize = ref(0);
      const fieldMessage = ref('');
      
      const soilResult = ref('');
      
      const seeds = ref([
        { id: 1, name: '水稻' },
        { id: 2, name: '小麦' },
        { id: 3, name: '玉米' },
      ]);
      const selectedSeed = ref('');
      const selectedSeedMessage = ref('');
  
      const manageField = () => {
        fieldMessage.value = `您已成功管理农田: ${fieldName.value}, 面积: ${fieldSize.value} 亩.`;
        // 重置输入
        fieldName.value = '';
        fieldSize.value = 0;
      };
  
      const testSoil = () => {
        soilResult.value = '土壤检测结果: PH 6.5, 有机质 3.2%';
      };
  
      const selectSeed = () => {
        selectedSeedMessage.value = `您已选择种子: ${selectedSeed.value}`;
      };
  
      return {
        fieldName,
        fieldSize,
        fieldMessage,
        soilResult,
        seeds,
        selectedSeed,
        selectedSeedMessage,
        manageField,
        testSoil,
        selectSeed,
      };
    },
  };
  </script>
  
  <style scoped>
  .planting-service {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
  }
  
  h1, h2 {
    color: #333;
  }
  
  label {
    display: block;
    margin: 10px 0 5px;
  }
  
  input, select, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
  }
  
  button {
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>