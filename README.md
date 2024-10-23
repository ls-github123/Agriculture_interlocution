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