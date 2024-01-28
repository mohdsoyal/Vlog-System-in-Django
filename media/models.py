from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# add the pic in profile..........
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE ,related_name='profile')
    image=models.ImageField(upload_to='pics',default='default.svg')



# find the hasing password..........
class Userpassword(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    
    def __str__(self):
        return self.username
    


class vlog_category(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

class vlog_contain(models.Model):
    title=models.CharField(max_length=100)
    des=models.TextField()
    date=models.DateField()
    image=models.TextField()
    category=models.ForeignKey(vlog_category,on_delete=models.CASCADE)    
