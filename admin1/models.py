from django.db import models

class admindb(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    email=models.CharField(max_length=40,null=True)
    name=models.CharField(max_length=40)
    add=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    mob_no=models.BigIntegerField()

class deliveryexec(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=200)
    mob_no=models.BigIntegerField()
    add=models.CharField(max_length=200)
    vehicle_trype=models.IntegerField()
    onleave=models.BooleanField()
    rating=models.IntegerField()

