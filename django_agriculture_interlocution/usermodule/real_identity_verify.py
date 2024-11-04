# 身份证实名认证接口封装
import httpx
import ssl

# APPCODE调用方法
async def check_id_card(name, idcard, appcode):
    host = 'https://kzidcardv1.market.alicloudapi.com'
    path = '/api-mall/api/id_card/check'
    url = host + path
    
    # 请求头参数
    headers = {
        'Authorization': f'APPCODE {appcode}',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    
    # 请求体参数
    bodys = {
        'name': name,
        'idcard': idcard
    }
    
    # 创建SSL 上下文, 忽略证书验证
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    # 使用异步客户端发送请求
    async with httpx.AsyncClient(verify=context) as client:
        try:
            response = await client.post(url, data=bodys, headers=headers)
            response.raise_for_status()  # 如果请求失败则引发异常
            return response.json()  # 返回 JSON 格式的响应内容
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            return None