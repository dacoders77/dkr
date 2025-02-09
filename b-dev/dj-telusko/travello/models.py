from django.db import models

# Create your models here.

class Destination(models.Model):
    #id: int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics') # Root media folder is set in settings
    desc = models.TextField(default='')
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)
