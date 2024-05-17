from unittest.main import MODULE_EXAMPLES
from django.db import models

# Create your models here.
class calorie(models.Model):
    username=models.CharField(max_length=20)
    batchno=models.CharField(max_length=20)
    foods=models.CharField(max_length=20)
    
class conta(models.Model):
    fullname=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    contactno=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    region=models.CharField(max_length=20)
    postalcode=models.CharField(max_length=20)