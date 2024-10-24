// Authing 登录集成配置 -- OAuth2 授权码模式
import axios from "axios";

const AUTHING_CONFIG = {
    appId: '671a02c6ef4cdd625a133fcd', // Authing App ID
    appHost: 'https://agricultureinterlocution.authing.cn', // Authing 认证(应用)地址
    redirectUri: 'http://localhost:5173/dashboard', // 登录回调地址
};

// 跳转到Authing托管登录页
// ${AUTHING_CONFIG.appHost}/oidc/auth -- Authing授权端点(用户登录和获取授权码)
// client_id=${AUTHING_CONFIG.appId} -- Authing应用ID,标识托管的应用
// redirect_uri -- 登录后重定向地址
// response_type=code 指定使用授权码模式
// scope=openid profile email 请求的权限范围
export function redirectToAuthing() {
    const authUrl = `${AUTHING_CONFIG.appHost}/oidc/auth`+
    `?client_id=${AUTHING_CONFIG.appId}`+
    `&redirect_uri=${encodeURIComponent(AUTHING_CONFIG.redirectUri)}`+
    `&response_type=code&scope=openid profile email`;

    window.location.href = authUrl; //页面重定向到 Authing 托管登录页
}

// 根据授权码获取access_token
export async function fetchAccessToken(code) {
    const tokenUrl = `${AUTHING_CONFIG.appHost}/oidc/token`;
    const data = new URLSearchParams({
        grant_type: 'authorization_code', // 授权类型:授权码模式
        client_id: AUTHING_CONFIG.appId, // 应用 ID
        code: code, // 授权码
        redirect_uri: AUTHING_CONFIG.redirectUri, //回调地址
    });

    try {
        const response = await axios.post(tokenUrl, data); // 请求access_token
        return response.data.access_token; // 返回access_token
    } catch (error) {
        console.error('获取access_token失败:', error);
        throw error;
    }
}