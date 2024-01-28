from django.forms import ModelForm
from .models import vlog_category,vlog_contain
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms


# create the contain in template.........
class vlog_form(ModelForm):
    class Meta:
        model=vlog_contain
        fields=['title','des','date','image','category']
        
        
# this is a own singup form......... 
class createform(UserCreationForm):
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email','password1','password2']
        labels ={'password':'Email'}
        
        
        
        
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter username'}),
            'first_name':forms.TextInput(attrs={'placeholder':'Enter first Name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter Email'}),
           'password1': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
           'password2': forms.PasswordInput(attrs={'placeholder': 'Enter Confirm Password'}),

        }
    
    


   

           
        
        
        
        