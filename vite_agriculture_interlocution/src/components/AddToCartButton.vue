<template>
    <button @click="addToCart(product.id)">加入购物车</button>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: {
      product: Object
    },
    methods: {
      async addToCart(productId) {
        try {
          await axios.post('http://localhost:8000/api/cart/add/', { product_id: productId, quantity: 1 });
          this.$emit('added', productId); // 通知父组件更新购物车
        } catch (error) {
          console.error('Failed to add product to cart:', error);
        }
      }
    }
  };
  </script>
  