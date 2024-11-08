from django.db import models

# Create your models here.


from django.db import models

# Create your models here.

class HarvestRequest(models.Model):
    # 定义作物类型选择
    CROP_TYPE = [
        (1, "小麦"),
        (2, "玉米"),
        (3, "大豆"),
        (4, "其他"),  # 修正了“其它”为“其他”
    ]
    
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField()
    cropType = models.IntegerField(choices=CROP_TYPE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'harvesting'
        verbose_name = '收割'
        verbose_name_plural = '收割'

class IrrigationRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    crop_type = models.CharField(max_length=50)
    irrigation_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.crop_type} - {self.irrigation_type}"
    
class Crop(models.Model):
    name = models.CharField(max_length=100)
    plantingdate = models.DateField()

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'crop'
        verbose_name = '种植'
        verbose_name_plural = '种植'