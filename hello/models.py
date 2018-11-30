from django.db import models
from datetime import datetime

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


# Create your models here.
class Mdata(models.Model):
    published_at = models.DateTimeField(default=datetime.now, blank=True)
    device_id = models.CharField(max_length=100)
    battery = models.DecimalField(decimal_places=2, max_digits=5)
    temp = models.DecimalField(decimal_places=2, max_digits=5)
    pressure = models.IntegerField()