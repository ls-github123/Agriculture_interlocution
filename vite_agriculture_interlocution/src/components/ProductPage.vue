<template>
  <div>
    <h1>商品列表</h1>
    <div v-for="product in products" :key="product.id" class="product">
      <p>{{ product.name }} - {{ product.price }}元</p>
      <button @click="addToCart(product.id)">加入购物车</button>
    </div>
    
    <!-- 跳转到购物车页面的按钮 -->
    <div class="cart-btn">
      <button @click="goToCart">查看购物车</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      products: []
    };
  },
  created() {
    this.fetchProducts();
  },
  methods: {
    // 获取商品列表
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost:8000/api/products/');
        this.products = response.data;
      } catch (error) {
        console.error('Failed to fetch products:', error);
      }
    },

    // 将商品添加到购物车
    async addToCart(productId) {
      try {
        await axios.post('http://localhost:8000/api/cart/add/', { product_id: productId, quantity: 1 });
        alert('商品已加入购物车');
      } catch (error) {
        console.error('Failed to add product to cart:', error);
      }
    },

    // 跳转到购物车页面
    goToCart() {
      this.$router.push('/cart');
    }
  }
};
</script>
