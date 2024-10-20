import os
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from .models import Product
from .forms import ProductForm  # ProductFormをインポート

# 商品一覧表示
def product_list_view(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)  # 1ページあたり10件
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/app.html', {'page_obj': page_obj})  # page_objをテンプレートに渡す

# 商品作成ビュー（関数ベース）
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # 新しい商品を保存
            return redirect('product_list')  # 商品一覧にリダイレクト
    else:
        form = ProductForm()
    
    return render(request, 'app/app.html', {'form': form})  # 正しいテンプレートを指定

# 商品更新ビュー（関数ベース）
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)  # 主キーに基づいて商品を取得
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()  # フォームの内容で商品を更新
            return redirect('product_list')  # 商品一覧にリダイレクト
    else:
        form = ProductForm(instance=product)  # 商品のデータを使ってフォームを作成

    return render(request, 'app/app.html', {'form': form})

# クラスベースのビュー
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm  # Formクラスを指定
    template_name = 'app/product_form.html'  # テンプレートを指定

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm  # Formクラスを指定
    template_name = 'app/product_form.html'  # 編集用テンプレートを指定
    success_url = '/app/'  # 更新後のリダイレクト先
