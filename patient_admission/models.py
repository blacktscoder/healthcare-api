from django.db import models

class Patient(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    gender = models.CharField(max_length=10)
    admitted_on = models.DateTimeField(auto_now_add=True)


# Create your models here.
