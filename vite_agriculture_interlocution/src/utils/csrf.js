// 从 Cookie 中提取 CSRF Token
export function getCSRFToken() {
    const match = document.cookie.match(/csrftoken=([^;]*)/);
    return match ? match[1] : null;
}