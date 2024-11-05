import axios from 'axios';
import { getCSRFToken } from './csrf';
import { refreshAccessToken } from './authing';

// 创建Axios实例
const apiClient = axios.create({
    baseURL:'http://127.0.0.1:8000/', // 后端api地址
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken(),  // 添加 CSRF Token
    },
    withCredentials: true, // 确保发送cookie
});

// 请求拦截器: 在每个请求中添加 CSRF TOKEN 和 Access Token
apiClient.interceptors.request.use(
    async (config) => {
        const csrftoken = getCSRFToken();
        if (csrftoken) {
            config.headers['X-CSRFToken'] = csrftoken;
        }

        let accessToken = sessionStorage.getItem('access_token');

        // 检查 AccessToken是否存在，若无则尝试刷新
        if (!accessToken) {
            await refreshAccessToken();
            accessToken = sessionStorage.getItem('access_token');
        }

        // 添加 Authorization Header
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
        }

        return config;
    },
    (error) => Promise.reject(error)
);

export default apiClient;