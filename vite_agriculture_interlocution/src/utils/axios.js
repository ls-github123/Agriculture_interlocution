import axios from 'axios';
import { getCSRFToken } from './csrf';

// 创建Axios实例
const apiClient = axios.create({
    baseURL:'http://127.0.0.1:8000/', // 后端api地址
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken(),  // 添加 CSRF Token
    },
    withCredentials: true, // 确保发送cookie
});

// 请求拦截器: 在每个请求中添加 CSRF TOKEN
apiClient.interceptors.request.use((config) => {
    const csrftoken = getCSRFToken();
    if (csrftoken) {
        config.headers['X-CSRFToken'] = csrftoken; // 设置 CSRF Token
    }
    const accessToken = sessionStorage.getItem('access_token');
    if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`;
    }
    return config;
}, (error) => Promise.reject(error));

export default apiClient;