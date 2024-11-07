# Generated by Django 5.1.2 on 2024-11-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customized', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IrrigationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('crop_type', models.CharField(max_length=50)),
                ('irrigation_type', models.CharField(max_length=50)),
            ],
        ),
    ]