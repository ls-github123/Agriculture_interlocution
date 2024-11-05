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
    proxy: {
      '/oidc': {
        target: 'https://agricultureinterlocution.authing.cn',
        changeOrigin: true,
        // 可选配置，用于处理 SSL 证书问题
        // secure: false,
      },
    },
  },
});