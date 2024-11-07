import axios from 'axios';
import { getCSRFToken } from './csrf';
import { refreshAccessToken, isTokenExpired, getAccessToken } from './authing';
import { logoutAndRedirect } from './authing';

// 创建Axios实例
const apiClient = axios.create({
    baseURL:'http://127.0.0.1:8000/', // 后端api地址
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: true, // 确保发送cookie
});

// 请求拦截器: 在每个请求中添加 CSRF TOKEN 和 Access Token
apiClient.interceptors.request.use(
    async (config) => {
        try {
            // 添加 CSRF Token(如果需要)
            const csrftoken = getCSRFToken();
            if (csrftoken) {
                config.headers['X-CSRFToken'] = csrftoken;
            } else {
                console.warn('CSRF Token 不存在，某些请求可能会失败');
            }

            // 获取 Access Token
            let accessToken = getAccessToken();

            // 检查 AccessToken 是否存在(用户是否登录)
            if (accessToken) {
                // 检查是否过期
                if (isTokenExpired(accessToken)) {
                    console.log('Access Token 已过期，尝试刷新 Token');
                    // 尝试刷新 Access Token
                    const success = await refreshAccessToken();
                    if (!success) {
                        // 刷新失败, 执行登出操作
                        logoutAndRedirect();
                        return Promise.reject(new Error('未授权, 请重新登录'));
                    }
                    accessToken = getAccessToken(); // 获取新的 Access Token
                }

                // 添加 Authorization 头
                if (accessToken) {
                    config.headers.Authorization = `Bearer ${accessToken}`;
                }
            }
            // 未登录用户, 不添加 Authorization 头
            return config;
        } catch (error) {
            // 捕获并处理请求拦截器中的错误
            console.error('请求拦截器发生错误:', error);
            return Promise.reject(error);
        }
    },
    (error) => Promise.reject(error)
);

// 响应拦截器：处理服务器返回的错误，例如 401 未授权
apiClient.interceptors.response.use(
    (response) => response,
    (error) => {
        // 如果服务器返回 401 未授权错误
        if (error.response && error.response.status === 401) {
            console.warn('401 未授权错误，执行登出操作');
            logoutAndRedirect();
        } else {
            // 捕获其他响应错误状态码
            const status = error.response?.status || '未知错误';
            console.error(`服务器响应错误: ${status}`, error);
        }
        return Promise.reject(error);
    }
);

export default apiClient;