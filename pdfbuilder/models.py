from django.db import models


class Seller(models.Model):
    sname= models.CharField(max_length=300, unique=True)
    sphone= models.IntegerField()
    saddress=models.CharField(max_length=300, unique=True)
    
class  Customer(models.Model):
    sname= models.CharField(max_length=300, unique=True)
    sphone= models.IntegerField()
    saddress=models.CharField(max_length=300, unique=True)
    
