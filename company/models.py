from django.db import models
# Create your models here.
class companydb(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    #verify=models.BooleanField(default=False)
    def __str__(self):
        return self.id

class curr_del(models.Model):
    del_id=models.CharField(max_length=10,primary_key=True)
    cust_name=models.CharField(max_length=40)
    cust_add=models.CharField(max_length=200)
    cust_contact=models.BigIntegerField()
    order_cap=models.IntegerField()
    delivered=models.BooleanField(default=False)
    cmp_id=models.ForeignKey(companydb,on_delete=models.CASCADE)

class delivery_data(models.Model):
    data_id=models.CharField(max_length=10,primary_key=True)
    cmp_id=models.CharField(max_length=10)
    new_del=models.FileField()
    uploaded_at=models.DateTimeField(auto_now_add=True)

class delivery_log(models.Model):
    del_id=models.CharField(max_length=10,primary_key=True)
    cust_name=models.CharField(max_length=40)
    cust_add=models.CharField(max_length=200)
    cust_contact=models.BigIntegerField()
    cmp_id=models.ForeignKey(companydb,on_delete=models.CASCADE)
    del_date=models.DateField()

