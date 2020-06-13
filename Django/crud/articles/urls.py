"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# 복사한 urls.py 임
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.index), #게시글 목록
    # send / receive
    path('new/',views.new), #<- 게시글 작성 양식
    path('create/',views.create), #<-게시글
    path('detail/<int:pk>/', views.detail),
    path('delete/<int:pk>/',views.delete),
    path('edit/<int:pk>/' , views.edit), #게시글 수정양식(GET)
    path('update/<int:pk>/', views.update) #게시글 수정!(POST)
]
