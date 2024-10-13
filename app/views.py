import os
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import Product

class TopView(TemplateView):
    template_name = "top.html"

#class ProductListView(ListView):
#    model = Product
#    paginate_by = 2
#    template_name = "app.html"

#以下自力で関数設定するのです<urls.pyも忘れずに>

def product_list(request):
    products = Product.objects.all()  # 商品を全件取得
    paginator = Paginator(products, 2)
    
    # 現在のページ番号を取得
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    return render(request, 'app.html', {'page_obj': page_obj})

class ProductCreateView(CreateView):
     model = Product
     fields = '__all__'

#def home_view(request):
#    return HttpResponse("<h1>ホームページ</h1><p>ようこそ！</p>")