from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    image=models.ImageField(upload_to="uploads/",max_length=250,null=True,default=None)
    description=models.CharField(max_length=300)
   
