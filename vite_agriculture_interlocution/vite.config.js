import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/oidc': {
        target: 'https://agricultureinterlocution.authing.cn',
        changeOrigin: true,
      },
    },
  },
});
