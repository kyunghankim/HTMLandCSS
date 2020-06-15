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

app_name = 'articles'


urlpatterns = [
    # 1. GET /articles/
    path('', views.index, name='index'), #게시글 목록
    # send / receive
    # 2. GET / articles/new/
    path('new/', views.new, name='new'), #<- 게시글 작성 양식
    # 3. POST / articles/new/
    # path('create/', views.create, name='create'), #<-게시글
    # 4. GET /articles/1/
    path('<int:pk>/', views.detail, name='detail'),
    # 5. POST(<-DELETE) /articles/1/ :update역할
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 6. GET /articles/edit/1/
    path('<int:pk>/edit/' , views.edit, name='edit'), #게시글 수정양식(GET)
    # #7. PUT,POST /articles/update/1/
    # path('update/<int:pk>/', views.update, name='update') #게시글 수정!(POST)
    # 
]
