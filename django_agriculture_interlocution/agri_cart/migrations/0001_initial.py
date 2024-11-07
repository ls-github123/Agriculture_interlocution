# Generated by Django 5.1.2 on 2024-11-06 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="agr_Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="agr_Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="商品名")),
                ("description", models.TextField(verbose_name="商品描述")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="价格"
                    ),
                ),
                ("stock", models.IntegerField(verbose_name="库存")),
            ],
        ),
        migrations.CreateModel(
            name="agr_CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(default=1, verbose_name="数量"),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agri_cart.agr_cart",
                        verbose_name="购物车",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agri_cart.agr_product",
                        verbose_name="商品",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="agr_cart",
            name="products",
            field=models.ManyToManyField(
                through="agri_cart.agr_CartItem", to="agri_cart.agr_product"
            ),
        ),
    ]