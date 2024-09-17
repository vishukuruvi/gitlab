from django.db import models

# Create your models here.
class Userdata(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    email=models.EmailField(max_length=25)
    mobile=models.IntegerField()
    add=models.CharField(max_length=25)
    pin=models.IntegerField()
    password=models.CharField(max_length=25)
