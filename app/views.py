from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    paginate_by = 2
    template_name = "app.html"

#以下自力で関数設定するのです<urls.pyも忘れずに>
