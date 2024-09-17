from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Userdata
from django.core.mail import send_mail
from django.conf import settings    

def hi(request):
    return render(request,'form.html')

def home(request):
    return render(request,'form1.html')

def home1(request):
    return render(request,'form0.html')

def after_reg(request):
    print(request.method)
    data_base = Userdata.objects.all()
    name=request.POST.get('first') + " " + request.POST.get('last')
    age=request.POST.get('age')
    email=request.POST.get('email')
    mobile=request.POST.get('mobile')
    add=request.POST.get('add')
    pin=request.POST.get('pin')
    password=request.POST.get('password')
    user_data= Userdata(name=name,age=age,email=email,mobile=mobile,add=add,pin=pin,password=password)
    user_data.save()
    return redirect('home')

def index0(request):
    print(request.method)
    data_base = Userdata.objects.all()
    name = request.POST.get('name')
    age = request.POST.get('age')
    email=request.POST.get('email')
    mobile=request.POST.get('mobile')
    add = request.POST.get('add')
    pin=request.POST.get('pin')
    password=request.POST.get('password')
    if password == "2002":
        return render(request,'form2.html',{'name':name,'age':age,'email':email,'mobile':mobile,'add':add,'pin':pin})
    else:
        return render(request,'form6.html')

def index1(request):
    print(request.method)
    data_base= Userdata.objects.all()
    password=request.POST.get('password')
    user_data= Userdata(password=password)
    #user_data.save()
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       body = request.POST.get('body')
       print(name,email,body)
       send_mail(
            'ITTamil - Chat',
            name + "-" + body ,
            email,
            ['django00@gmail.com'],
            fail_silently = False,
        )
        #return render(request,'form3.html')
    return render(request,'form3.html',{'password': password})

def dark(request):
    return render(request,'form5.html')

def uploadphoto(request):
    return render(request,'photo.html')

def speedtest(request):
    template = loader.get_template('form4.html')
    res = template.render ({}, request)
    return HttpResponse(res)
