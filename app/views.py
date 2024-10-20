import os
from django.core.paginator import Paginator
from django.shortcuts import render, redirect  # redirectを追加
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm  # ProductFormをインポート

# 商品一覧表示
def product_list_view(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)  # 1ページあたり10件
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/app.html', {'object_list': page_obj})

#   return render(request, 'app.html', {'page_obj': page_obj})

# 商品作成ビュー（関数ベース）
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # 商品を保存
            return redirect('product_list')  # 作成後に商品一覧へリダイレクト
    else:
        form = ProductForm()  # GETリクエスト時は空のフォームを表示

    return render(request, 'app/product_form.html', {'form': form})
