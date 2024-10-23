# Generated by Django 5.1.2 on 2024-10-23 12:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='邮箱')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='电话号码')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
        ),
    ]
