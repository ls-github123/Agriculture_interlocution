from django.db import models

# Create your models here.

class AgricultureKnowledge(models.Model):
    id = models.CharField(max_length=100, primary_key=True)  # 唯一标识符
    title = models.CharField(max_length=255)  # 标题
    content = models.TextField()  # 内容
    category = models.CharField(max_length=100)  # 类别
    author = models.CharField(max_length=100)  # 作者
    date = models.DateTimeField(auto_now_add=True)  # 创建日期
    tags = models.CharField(max_length=255)  # 标签

    def __str__(self):
        return self.title  # 返回标题作为字符串表示