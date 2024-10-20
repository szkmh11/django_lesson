<<<<<<< HEAD:Django_Lesson/Django_Lesson/app/views.py
import os
from django.core.paginator import Paginator
from django.shortcuts import render, redirect  # redirectを追加
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm  # ProductFormをインポート
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

# 商品一覧表示
def product_list_view(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)  # 1ページあたり10件
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/app.html', {'object_list': page_obj})

#   return render(request, 'app.html', {'page_obj': page_obj})

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

#商品作成ビュー（関数ベース）
def product_create(request):
   if request.method == 'POST':
       form = ProductForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('product_list')  # 商品一覧ページにリダイレクト
   else:
       form = ProductForm()
   return render(request, 'app/product_form.html', {'form': form})

#編集ビュー
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'


#編集ビュー（関数ベース）
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)  # 主キーに基づいて商品を取得

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()  # フォームの内容で商品を更新
            return redirect('product_list')  # 商品一覧にリダイレクト
    else:
        form = ProductForm(instance=product)  # 商品のデータを使ってフォームを作成

    return render(request, 'app/product_form.html', {'form': form})
=======
import os
from django.core.paginator import Paginator
from django.shortcuts import render, redirect  # redirectを追加
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm  # ProductFormをインポート
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.db import models

# 商品一覧表示
def product_list_view(request):
    product_list = Product.objects.all().order_by('id')  # idの昇順で並び替え
    paginator = Paginator(product_list, 10)  # 1ページあたり10件
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/app.html', {'object_list': page_obj})

#   return render(request, 'app.html', {'page_obj': page_obj})

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

#商品作成ビュー（関数ベース）
def product_create(request):
   if request.method == 'POST':
       form = ProductForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('product_list')  # 商品一覧ページにリダイレクト
   else:
       form = ProductForm()
   return render(request, 'app/product_form.html', {'form': form})

#編集ビュー
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'


#編集ビュー（関数ベース）
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'app/product_form.html', {'form': form})

# 商品詳細表示ビュー
# def product_detail_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)  # 主キーに基づいて商品を取得
#     return render(request, 'app/product_detail.html', {'product': product})
>>>>>>> 7b3be38 (10202130　無事に動きました):app/views.py
