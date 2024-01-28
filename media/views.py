from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import vlog_contain
from .forms import vlog_form ,createform
from .models import Userpassword


# Create your views here.


def index(request):
    data=vlog_contain.objects.all().order_by("?")
    return render(request,'index.html',{'data':data})

def vlog_dashboard(request):
    data=vlog_contain.objects.all()
    return render(request,'vlog-dashboard.html',{'data':data})

def vlog_create(request):
    fm=vlog_form()
    data=vlog_contain.objects.all()
    if request.method =='POST':
        fm=vlog_form(request.POST, request.FILES)
        if fm.is_valid():
            title=fm.cleaned_data['title']
            des=fm.cleaned_data['des']
            date=fm.cleaned_data['date']
            image=fm.cleaned_data['image']
            category=fm.cleaned_data['category']
            saved=vlog_contain(title=title,des=des,date=date,image=image,category=category)
            saved.save()
            fm=vlog_form()   
    return render(request,'vlog-create.html',{'fm':fm,'data':data})
      

def vlog_update(request,id):
    data=vlog_contain.objects.get(id=id)
    if request.method == 'POST':
        fm=vlog_form(request.POST,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('vlog-dashboard')
    else:
     fm=vlog_form(instance=data)
    return render(request,'vlog-update.html',{'fm':fm})

def delete_vlog(request,id):
    data=vlog_contain.objects.get(id=id)
    data.delete()
    return redirect('vlog-dashboard')

def single_page(request,id):
    data=vlog_contain.objects.get(id=id)
    return render(request,'single-page.html',{'data':data})

def search(request):
   if request.method =='GET':
       st=request.GET.get('search')
       data=vlog_contain.objects.filter(title__icontains=st)
       return render(request,'search.html',{'data':data,'st':st})

def login_page(request):
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        Userpassword(username=username,password=password).save()
        if user is not None:
            request.session['username']=username
            login(request,user)
            return redirect('profile')
    else:
      return render(request,'login.html')
        

def signup(request):
    if request.method =='POST':
        fm=createform(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            first_name=fm.cleaned_data['first_name']
            last_name=fm.cleaned_data['last_name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password1']
            password=make_password(password)
            saved=User(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            saved.save()
            login(request,saved)
            return redirect('index')
    else:
       fm=createform()      
    return render(request,'signup.html',{'fm':fm})


def logouts(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render
from django.contrib.auth.models import User  # Make sure to import the User model if you haven't already

from django.shortcuts import render
from django.contrib.auth.models import User  # Make sure to import the User model if you haven't already

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    
    else:
        return redirect('login')