from django.db import models

# Create your models here.
class data_sent(models.Model):
    Temp_IoT = models.IntegerField()
    Humi_IoT = models.IntegerField()
    Device_IoT = models.CharField(max_length=50)
    time_IoT = models.DateTimeField(auto_now_add=True)