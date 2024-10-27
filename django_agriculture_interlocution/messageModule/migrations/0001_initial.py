# Generated by Django 5.1.2 on 2024-10-27 11:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MessageType",
            fields=[
                (
                    "type_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="类型ID"
                    ),
                ),
                ("type_name", models.CharField(max_length=50, verbose_name="类型名称")),
                (
                    "icon_url",
                    models.URLField(blank=True, null=True, verbose_name="图标URL"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="创建时间"
                    ),
                ),
            ],
            options={
                "verbose_name": "消息类型",
                "verbose_name_plural": "消息类型",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="用户ID"
                    ),
                ),
                ("username", models.CharField(max_length=50, verbose_name="用户名")),
                ("password", models.CharField(max_length=255, verbose_name="密码")),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=100, null=True, verbose_name="邮箱"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="电话号码"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="创建时间"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="最后更新时间"),
                ),
            ],
            options={
                "verbose_name": "用户",
                "verbose_name_plural": "用户",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "message_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="消息ID"
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="消息标题")),
                ("content", models.TextField(verbose_name="消息内容")),
                (
                    "send_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="发送时间"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("unread", "未读"),
                            ("read", "已读"),
                            ("deleted", "已删除"),
                        ],
                        default="unread",
                        max_length=20,
                        verbose_name="消息状态",
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[("low", "低"), ("medium", "中"), ("high", "高")],
                        default="medium",
                        max_length=20,
                        verbose_name="优先级",
                    ),
                ),
                (
                    "read_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="阅读时间"
                    ),
                ),
                (
                    "attachments",
                    models.JSONField(blank=True, null=True, verbose_name="附件"),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="消息分类"
                    ),
                ),
                (
                    "tags",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="标签"
                    ),
                ),
                (
                    "type_id",
                    models.ForeignKey(
                        db_column="type_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="messageModule.messagetype",
                        verbose_name="类型ID",
                    ),
                ),
                (
                    "receiver_id",
                    models.ForeignKey(
                        db_column="receiver_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
                        to="messageModule.user",
                        verbose_name="接收者ID",
                    ),
                ),
                (
                    "sender_id",
                    models.ForeignKey(
                        db_column="sender_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to="messageModule.user",
                        verbose_name="发送者ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "消息",
                "verbose_name_plural": "消息",
            },
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "feedback_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="反馈ID"
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=1000, verbose_name="反馈描述"),
                ),
                (
                    "problem_type",
                    models.CharField(
                        choices=[
                            ("功能建议", "功能建议"),
                            ("页面问题", "页面问题"),
                            ("操作问题", "操作问题"),
                            ("功能问题", "功能问题"),
                            ("购买问题", "购买问题"),
                            ("其他", "其他"),
                        ],
                        max_length=50,
                        verbose_name="问题类型",
                    ),
                ),
                (
                    "contact_person",
                    models.CharField(max_length=50, verbose_name="联系人"),
                ),
                (
                    "contact_phone",
                    models.CharField(max_length=20, verbose_name="联系电话"),
                ),
                (
                    "attachment_urls",
                    models.JSONField(default=list, verbose_name="附件URL数组"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="messageModule.user",
                        verbose_name="用户ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "反馈",
                "verbose_name_plural": "反馈",
            },
        ),
    ]
