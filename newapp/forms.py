from django import forms
from .models import *
from django.contrib.auth.models import User
class regform(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    uname=forms.CharField(max_length=50)
    email=forms.EmailField()
    address=forms.CharField(max_length=100)
    phone=forms.IntegerField()
    password=forms.CharField(max_length=10)
    cpassword=forms.CharField(max_length=10)

class logform(forms.Form):
    uname=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)


class adminform(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField()


class productform(forms.Form):
    productname=forms.CharField(max_length=50)
    productid=forms.CharField(max_length=10)
    price=forms.IntegerField()
    description=forms.CharField(max_length=500)
    file=forms.FileField()

class fileform(forms.ModelForm):
    class Meta:
        model=productmodel
        fields='__all__'


class buyform(forms.Form):
    uname=forms.CharField(max_length=30)
    phone=forms.IntegerField()
    address=forms.CharField(max_length=100)
    price = forms.IntegerField()
    mode=forms.CharField(max_length=30)
    # quantity = forms.IntegerField()

