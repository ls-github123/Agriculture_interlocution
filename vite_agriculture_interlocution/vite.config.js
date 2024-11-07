import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, '/src'), // 配置路径别名
    },
  },
  server: {
    host : '127.0.0.1',
    port : 5173,
    proxy: {
      // 代理请求到 Django 后端
      '/api': {
        target: 'http://127.0.0.1:8000', // Django 后端的地址
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''), // 去掉 /api 前缀，方便后端处理
      },
      '/oidc': {
        target: 'https://agricultureinterlocution.authing.cn',
        changeOrigin: true,
        // 可选配置，用于处理 SSL 证书问题
        // secure: false,
      },
    },
  },
});