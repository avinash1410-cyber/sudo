import email
from django.db import models
from django.forms import EmailField

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=13,blank=True,null=True)
    last_name=models.CharField(max_length=13,blank=True,null=True)
    mobileno=models.CharField(max_length=200,null=True,blank=True,unique=True)
    email=models.EmailField(null=True,blank=True,unique=True)
    def __str__(self):
        return str(self.first_name)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_no=models.CharField(max_length=13,blank=True,null=True,unique=True)

    def __str__(self):
        return str(self.user)
    @property
    def name(self):
        return self.__str__()