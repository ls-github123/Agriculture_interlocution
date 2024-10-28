# Agriculture_interlocution
P5实训项目——农业专家问答系统（李硕、刘鹏、宋金玺）

Windows端-powershell生成 SSH密钥对
使用 SSH 连接 如果 HTTPS 连接问题无法解决，可以尝试使用 SSH 连接 GitHub 仓库。首先，你需要生成一个 SSH 密钥对，并将公钥添加到 GitHub 账户

1.生成密钥对命令: ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
(-t rsa 指定密钥类型为 RSA \ -b 4096 指定密钥长度为 4096 位 \ -C "your_email@example.com" 添加注释（通常是你的电子邮件地址）)

2.查看公钥的 SHA256 指纹: ssh-keygen -lf ~/.ssh/id_rsa.pub -E sha256

# 为 p5_project_Agriculture_interlocution 仓库单独配置 SSH 密钥
Host Agriculture_interlocution
  HostName github.com
  User (本人姓名)
  IdentityFile  D:/ssh-key/....

# 在Conda环境中导出依赖包目录<-->根据依赖包目录导入对应依赖
# (导出 pip 依赖并让团队成员导入)
  导出并更新目录为requirements.txt文件命令 --> pip freeze > requirements.txt
  在新环境中使用 requirements.txt 安装 pip 依赖命令 --> pip install -r requirements.txt

  列出现有 Conda 虚拟环境的依赖命令 --> conda list

# 在标准 Web 应用中集成 Authing
  一共牵涉到三方：终端用户浏览器、应用服务器、 Authing 服务器，完整流程如下：

  1.终端用户浏览器请求应用服务，发现用户未登录，跳转到 Authing 托管的登录页。
  2.用户在此登录页完成登录之后，终端用户浏览器会在请求参数中携带授权码 (Authorization Code) 等数据跳转到应用服务器预先配置好的回调链。
  3.应用服务器使用授权码 (Authorization Code) 向 Authing 服务器请求换取用户信息。
  4.应用服务器获取到用户信息之后，建立与终端用户的会话。
  5.终端用户得到登录成功提示，认证流程完成。
  
  ![image](https://github.com/user-attachments/assets/b60f7b16-7f87-4678-a1f3-53db5c22fcdc)
