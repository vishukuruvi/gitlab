"""
URL configuration for vishuu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vishva import views

urlpatterns = [
    path('', views.hi),
    path('hi', views.hi,name='hi'),
    path('home', views.home,name='home'),
    path('home1', views.home1),
    path('index0', views.index0,name='index0'),
    path('index1', views.index1,name='index1'),
    path('after_reg',views.after_reg,name='after_reg'),
    path('dark',views.dark,name='dark'),
    path('uploadphoto',views.uploadphoto,name='uploadphoto'),
    path('speedtest' ,views.speedtest,name='speedtest'),
]
