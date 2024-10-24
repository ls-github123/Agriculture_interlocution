// Authing 登录集成配置 -- OAuth2 授权码模式
import axios from "axios";

const AUTHING_CONFIG = {
    appid: '67199a7561f7d9416af29037', // Authing App ID
    appHost: 'https://agriculture-interlocution.authing.cn', // Authing 认证(应用)地址
    redirectUri: 'http://localhost:5173/callback', // 登录回调地址
};

// 跳转到Authing托管登录页
export function redirectToAuthing() {
    const authUrl = `${AUTHING_CONFIG.appHost}/oidc/auth`+
    `?client_id=${AUTHING_CONFIG.appId}`+
    `&redirect_uri=${encodeURIComponent(AUTHING_CONFIG.redirectUri)}`+
    `&response_type=code&scope=openid profile email`;

    window.location.href = authUrl; //跳转到登录页面
}

