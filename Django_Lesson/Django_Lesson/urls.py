"""
URL configuration for Django_Lesson project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views
from app.views import product_create, product_update,product_list_view

urlpatterns = [
    path('', views.product_list_view, name='product_list'),
    path('admin/', admin.site.urls),
    # path('app/', views.product_list_view, name='product_list'),  # 修正
    path('app/new/', views.ProductCreateView.as_view(), name="new"),
    path('app/edit/<int:pk>',views.ProductUpdateView.as_view(), name="edit"),
    path('app/new/', views.product_create, name='new'), 
#    path('product/new/', product_create, name='product_create'),
    path('product/edit/<int:pk>/', product_update, name='product_update'),
]
