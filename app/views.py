import os
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product, Category  # Categoryモデルもインポート
from .forms import ProductForm  # ProductFormをインポート

# 商品一覧表示
def product_list_view(request):
    products = Product.objects.all()  # データベースから全商品を取得
    categories = Category.objects.all()  # カテゴリをすべて取得
    paginator = Paginator(products, 6)  # 1ページあたり6商品を表示
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app.html', {
        'page_obj': page_obj,
        'categories': categories,
    })

# カテゴリ別の商品フィルタ表示
def category_filter(request, id):
    products = Product.objects.filter(category_id=id)  # 指定カテゴリの商品のみ取得
    categories = Category.objects.all()  # すべてのカテゴリを取得
    paginator = Paginator(products, 6)  # 1ページあたり6商品を表示
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app.html', {
        'page_obj': page_obj,
        'categories': categories,
    })

# 商品作成ビュー（関数ベース）
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # 画像ファイルも受け取る場合はrequest.FILESを追加
        if form.is_valid():
            form.save()  # 新しい商品を保存
            return redirect('product_list')  # 商品一覧にリダイレクト
    else:
        form = ProductForm()
    
    return render(request, 'app/product_form.html', {'form': form})  # 作成フォーム用テンプレートを指定

# 商品更新ビュー（関数ベース）
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)  # 主キーに基づいて商品を取得
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()  # フォームの内容で商品を更新
            return redirect('product_list')  # 商品一覧にリダイレクト
    else:
        form = ProductForm(instance=product)  # 商品のデータを使ってフォームを作成

    return render(request, 'product_form.html', {'form': form})  # 編集フォーム用テンプレートを指定

# 商品削除ビュー（関数ベース）
@require_POST
def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()  # 商品を削除
    return redirect('product_list')  # 商品一覧にリダイレクト

# 以下はクラスベースのビューをコメントアウト
# class ProductCreateView(CreateView):
#     model = Product
#     form_class = ProductForm  # フォームクラスを指定
#     template_name = 'app/product_form.html'  # 作成フォーム用テンプレートを指定

# class ProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductForm  # フォームクラスを指定
#     template_name = 'app/product_form.html'  # 編集用テンプレートを指定
#     success_url = reverse_lazy('product_list')  # 更新後のリダイレクト先

# class ProductDeleteView(DeleteView):
#     model = Product
#     success_url = reverse_lazy('product_list')  # 削除後のリダイレクト先
