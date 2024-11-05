// Token 逻辑封装

import apiClient from "./axios";

// Authing 登录集成配置 -- OAuth2 授权码模式
const AUTHING_CONFIG = {
    appId: '671a02c6ef4cdd625a133fcd', // Authing App ID
    appHost: 'https://agricultureinterlocution.authing.cn', // Authing 认证(应用)地址
    redirectUri: 'http://localhost:5173/home', // 登录回调地址
};


// 跳转到Authing托管登录页
// ${AUTHING_CONFIG.appHost}/oidc/auth -- Authing授权端点(用户登录和获取授权码)
// client_id=${AUTHING_CONFIG.appId} -- Authing应用ID,标识托管的应用
// redirect_uri -- 登录后重定向地址
// response_type=code 指定使用授权码模式
// scope=openid profile email offline_access 请求的权限范围
export function redirectToAuthing() {
    const state = generateState(); // 生成唯一 state 值
    const authUrl = `${AUTHING_CONFIG.appHost}/oidc/auth`+
                    `?client_id=${AUTHING_CONFIG.appId}`+
                    `&response_type=code`+
                    `&scope=openid+profile+offline_access+username+email+phone`+ // 必须包含offline_access
                    `&redirect_uri=${encodeURIComponent(AUTHING_CONFIG.redirectUri)}`+
                    `&prompt=consent`+ // 强制用户同意授权
                    `&state=${state}`;
    sessionStorage.setItem('auth_state', state); // 保存 state 用于验证
    window.location.href = authUrl; //页面重定向到 Authing 托管登录页
}

// 生产随机 state 字符串
function generateState() {
    return Math.random().toString(36).substring(2, 15);
}

// 从 URL 中提取授权码
export function getAuthorizationCode() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('code');
}

// 判断令牌是否过期
export function isTokenExpired(token) {
    try {
        // 检查令牌的格式是否正确
        const parts = token.split('.');
       if (parts.length !== 3) throw new Error('无效的JWT格式');
        // Base64 解码 payload 部分，并解析为 JSON 对象
        const payload = JSON.parse(atob(parts[1]));
        if (!payload.exp) throw new Error('缺少 exp 字段');
        // 比较当前时间与 exp（到期时间）字段
        const currentTime = Math.floor(Date.now() / 1000); // 获取当前时间（秒）
        return currentTime >= payload.exp;  // 返回 true 表示已过期
    } catch (error) {
        console.error('解码令牌失败:', error);
        return true;  // 如果出现异常，认为令牌无效或已过期
    }
}

// 获取 refresh_token
export function getRefreshToken() {
    const match = document.cookie.match(/(^| )refresh_token=([^;]+)/);
    const token = match ? match[2] : null;
    console.log("获取到的 refresh_token:", token);
    return token;
}

// 刷新 Access Token
export async function refreshAccessToken() {
    const refreshToken = getRefreshToken();
    if (!refreshToken) {
        console.error('缺少 refresh_token, 请重新登录');
        // logoutAndRedirect();
        return;
    }
    try {
        const { data } = await apiClient.post('/user/refresh_token/', { refresh_token: refreshToken });
        storeTokens(data.access_token, data.id_token, refreshToken);
    } catch (error) {
        console.error('刷新令牌失败:', error);
        if (error.response?.status === 401) {
            // logoutAndRedirect();
        }
    }
}

// 存储 Tokens
export function storeTokens(accessToken, idToken, refreshToken) {
    storeAccessToken(accessToken);
    storeIdToken(idToken);
    storeRefreshToken(refreshToken);
    console.log('成功存储令牌');
}

// 存储 Access Token 到 sessionStorage
function storeAccessToken(token) {
    sessionStorage.setItem('access_token', token);
}

// 存储 ID Token 到 sessionStorage中
function storeIdToken(token) {
    sessionStorage.setItem('id_token', token);
}

// 存储 Refresh Token 到 HttpOnly Cookie 中
function storeRefreshToken(token) {
    console.log("存储 refresh_token:", token);
    document.cookie = `refresh_token=${token}; Max-Age=2592000; Path=/; Secure; SameSite=Lax`;
}


// 获取用户信息并存储
export async function fetchAndStoreUserInfo() {
    try {
        const { data: userInfo } = await apiClient.get('/user/user_info');
        storeUserInfo(userInfo);
    } catch (error) {
        console.error('获取用户信息失败:', error);
        throw new Error('获取用户信息失败，请重新登录!');
    }
}

// 存储用户信息到 sessionStorage
function storeUserInfo(userInfo) {
    sessionStorage.setItem('user_info', JSON.stringify(userInfo));
    console.log('用户信息已缓存');
}

// 获取用户信息
export function getUserInfo() {
    const userInfo = sessionStorage.getItem('user_info');
    return userInfo ? JSON.parse(userInfo) : null;
}

// 清除用户信息
function clearUserInfo() {
    sessionStorage.removeItem('user_info');
}

// 退出登录 -- 清理所有授权状态并登出
export function logoutAndRedirect() {
    clearAuthState();
    clearUserInfo();
    const logoutUrl = `${AUTHING_CONFIG.appHost}/oidc/session/end`+
                      `?post_logout_redirect_uri=${encodeURIComponent(window.location.origin)}`;
    window.location.href = logoutUrl;
}

// 清除本地授权状态
function clearAuthState() {
    sessionStorage.removeItem('access_token');
    sessionStorage.removeItem('id_token');
    document.cookie = 'refresh_token=; Max-Age=0; path=/;';
}

// 获取存储在 sessionStorage 中的 Access Token
export function getAccessToken() {
    return sessionStorage.getItem('access_token');
}

// 使用授权码获取令牌并存储
export async function fetchAndStoreTokens(code) {
    try {
        const { data } = await apiClient.post('/user/token/', { code });
        console.log('获取令牌成功:', data); // 添加调试信息
        storeTokens(data.access_token, data.id_token, data.refresh_token);
        await fetchAndStoreUserInfo(); // 获取并缓存用户信息
    } catch (error) {
        console.error('获取令牌失败:', error);
        logoutAndRedirect(); // 失败时重定向到退出
    }
}