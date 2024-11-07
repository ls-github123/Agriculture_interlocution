<template>
  <div class="product-list">
    <!-- 返回上一页按钮 -->
    <button class="back-btn" @click="goBack">← 返回</button>

    <h1 class="title">商品列表</h1>
    <div class="product-grid">
      <div v-for="product in products" :key="product.id" class="product-card">
        <!-- 商品图片 -->
        <div class="product-image">
          <img :src="product.image_url || 'https://via.placeholder.com/250x250.png?text=商品图片'" alt="Product Image">
        </div>

        <div class="product-info">
          <h3 class="product-name">{{ product.name }}</h3>
          <p class="product-price">{{ product.price }}元</p>
        </div>

        <button class="add-to-cart-btn" @click="addToCart(product.id)">加入购物车</button>
      </div>
    </div>
    
    <!-- 跳转到购物车页面的按钮 -->
    <div class="cart-btn-container">
      <button class="cart-btn" @click="goToCart">查看购物车</button>
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
        const response = await axios.get('http://localhost:8000/agri_cart/products/');
        this.products = response.data;
      } catch (error) {
        console.error('Failed to fetch products:', error);
      }
    },

    // 将商品添加到购物车
    async addToCart(productId) {
      try {
        await axios.post('http://localhost:8000/agri_cart/cart/add/', { product_id: productId, quantity: 1 });
        alert('商品已加入购物车');
      } catch (error) {
        console.error('Failed to add product to cart:', error);
      }
    },

    // 跳转到购物车页面
    goToCart() {
      this.$router.push('/cart');
    },

    // 返回上一页
    goBack() {
      window.history.back();
    }
  }
};
</script>

<style scoped>
/* 整体页面样式 */
.product-list {
  font-family: 'Arial', sans-serif;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

/* 返回上一页按钮 */
.back-btn {
  position: absolute;
  top: 20px;
  left: 20px;
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  font-size: 1.2em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.back-btn:hover {
  background-color: #0056b3;
}

/* 标题样式 */
.title {
  font-size: 2.5em;
  font-weight: bold;
  text-align: center;
  color: #333;
  margin-top: 60px; /* 增加顶部空间以避免与返回按钮重叠 */
  margin-bottom: 30px;
}

/* 商品网格布局 */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

/* 商品卡片 */
.product-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: #fff;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease-in-out;
}

.product-card:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}

/* 商品图片 */
.product-image {
  width: 100%;
  height: 250px; /* 图片的高度，确保一致 */
  overflow: hidden; /* 隐藏超出范围的部分 */
  border-radius: 8px;
  margin-bottom: 15px;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 确保图片覆盖整个区域并保持比例 */
}

/* 商品信息 */
.product-info {
  flex-grow: 1;
}

.product-name {
  font-size: 1.2em;
  font-weight: bold;
  margin: 0;
}

.product-price {
  font-size: 1em;
  color: #666;
  margin-top: 5px;
}

/* 加入购物车按钮 */
.add-to-cart-btn {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 10px;
}

.add-to-cart-btn:hover {
  background-color: #218838;
}

/* 跳转到购物车按钮 */
.cart-btn-container {
  text-align: center;
  margin-top: 30px;
}

.cart-btn {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 12px 25px;
  font-size: 1.1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.cart-btn:hover {
  background-color: #0056b3;
}
</style>
