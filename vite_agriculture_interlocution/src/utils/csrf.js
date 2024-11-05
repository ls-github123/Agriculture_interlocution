// 从 Cookie 中提取 CSRF Token
export function getCSRFToken() {
    const csrfToken = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1];

    if (!csrfToken) {
        console.warn('CSRF Token 未找到，请确保已设置 CSRF Cookie');
    }

    return csrfToken || null;
}