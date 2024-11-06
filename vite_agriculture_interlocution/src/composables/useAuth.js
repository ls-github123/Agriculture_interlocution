// 组合式 API 封装认证逻辑

// 导入 Vue 中必要的函数
import { ref } from "vue";

// 使用别名导入认证工具
import {
  getUserInfo,
  getAccessToken,
  isTokenExpired,
  redirectToAuthing,
  logoutAndRedirect,
} from "../utils/authing"; // 根据项目结构调整路径

// 定义 useAuth 组合式函数
export function useAuth() {
  // 使用 ref 定义 userInfo，因为它是一个单独的响应式属性
  const userInfo = ref(null);

  // 初始化，检查是否已认证并获取用户信息
  function init() {
    if (isAuthenticated()) {
      userInfo.value = getUserInfo();
    } else {
      userInfo.value = null;
    }
  }

  // 登录函数，重定向到 Authing
  function login() {
    redirectToAuthing();
  }

  // 登出函数，清除认证并重定向
  function logout() {
    logoutAndRedirect();
    userInfo.value = null; // 登出后清除 userInfo
  }

  // 检查用户是否已认证
  function isAuthenticated() {
    const token = getAccessToken();
    return token && !isTokenExpired(token);
  }

  // 返回响应式属性和方法
  return {
    userInfo,
    init,
    login,
    logout,
  };
}