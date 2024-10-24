import axios from 'axios';

// 创建Axios实例
const apiClient = axios.create({
    baseURL:'http://127.0.0.1:8000/', // 后端api地址
    headers: {
        'Content-Type': 'application/json',
    },
});

apiClient.interceptors.request.use((config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
}, (error) => {
    return Promise.reject(error);
});

export default apiClient;