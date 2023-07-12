from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class student(models.Model):
    First_Name=models.CharField(max_length = 70, default=None)  
    Last_Name=models.CharField(max_length = 70, default=None)  
    User_Name=models.CharField(max_length = 70, default=None)  
    Email=models.EmailField(max_length = 70, default=None)  
  
    image=models.ImageField(upload_to="image/",null=True) 
    