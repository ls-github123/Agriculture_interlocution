from .pay import AliPay


def get_alipay():
    # 初始化支付实例
   
    #公共参数
    # 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info
    app_id = "9021000140665917"  #  APPID （沙箱应用）

    # 支付完成后，支付偷偷向这里地址发送一个post请求，识别公网IP,如果是 192.168.20.13局域网IP ,支付宝找不到，def page2() 接收不到这个请求
    notify_url = "http://localhost:8000/api/alipay/notify/"

    # 支付完成后，跳转的地址。
    return_url = "http://localhost:5173/"

    merchant_private_key_path = "keys/private.txt" # 应用私钥
    alipay_public_key_path = "keys/public.txt"  # 支付宝公钥

    alipay = AliPay(
        appid=app_id,
        app_notify_url=notify_url,
        return_url=return_url,
        app_private_key_path=merchant_private_key_path,
        alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
        debug=True,  # 默认False,
    )
    return alipay