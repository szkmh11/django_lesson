from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    template_name = "app.html"


def read_products(request):
    """
    データの一覧を表示する
    """
    # 全オブジェクトを取得
    products = Product.objects.all()
    return render(request,
                  'product_list.html',  # 呼び出す Template
                  {'product_list': product_list})  # Template に渡すデータ