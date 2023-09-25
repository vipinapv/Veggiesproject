from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class regmodel(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    uname=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)

class productmodel(models.Model):
    productname=models.CharField(max_length=50)
    productid=models.CharField(max_length=10)
    price=models.IntegerField()
    description=models.CharField(max_length=500)
    file=models.FileField(upload_to='newapp/static')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.filename




class cart(models.Model):
    uid = models.IntegerField()
    productid=models.CharField(max_length=10)
    productname = models.CharField(max_length=50)
    productdescription = models.CharField(max_length=500)
    price=models.IntegerField()
    file=models.FileField(upload_to='newapp/static')
    date = models.DateField(auto_now_add=True)


class buy(models.Model):
    uid = models.IntegerField()
    uname=models.CharField(max_length=30)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    price=models.IntegerField()
    mode=models.CharField(max_length=30)
    # option1 = models.BooleanField()
    # option2 = models.BooleanField()
    # option3 = models.BooleanField()
