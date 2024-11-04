# Generated by Django 5.1.2 on 2024-11-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AgricultureKnowledge",
            fields=[
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("category", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("tags", models.CharField(max_length=255)),
            ],
        ),
    ]
