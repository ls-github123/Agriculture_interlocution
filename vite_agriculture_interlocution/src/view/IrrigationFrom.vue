<template>
  <div class="irrigation-form">
    <h2>灌溉服务申请表</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name">姓名：</label>
        <input type="text" id="name" v-model="formData.name" required />
      </div>
      <div class="form-group">
        <label for="phone">电话：</label>
        <input type="tel" id="phone" v-model="formData.phone" required />
      </div>
      <div class="form-group">
        <label for="address">地址：</label>
        <textarea id="address" v-model="formData.address" required></textarea>
      </div>
      <div class="form-group">
        <label for="cropType">作物类型：</label>
        <select id="cropType" v-model="formData.cropType" required>
          <option value="小麦">小麦</option>
          <option value="玉米">玉米</option>
          <option value="大豆">大豆</option>
          <option value="其它">其它</option>
        </select>
      </div>
      <div class="form-group">
        <label for="irrigationType">灌溉类型：</label>
        <select id="irrigationType" v-model="formData.irrigationType" required>
          <option value="滴灌">滴灌</option>
          <option value="喷灌">喷灌</option>
          <option value="漫灌">漫灌</option>
          <option value="其它">其它</option>
        </select>
      </div>
      <button type="submit">提交申请</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const formData = ref({
  name: '',
  phone: '',
  address: '',
  cropType: '',
  irrigationType: ''
});

const handleSubmit = async () => {
  try {
    const response = await axios.post('http://localhost:8000/api/irrigation/', formData.value);
    alert('申请成功！');
    console.log(response.data);
  } catch (error) {
    console.error('申请失败:', error);
    alert('申请成功。');
  }
};
</script>

<style scoped>
.irrigation-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, textarea, select {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>