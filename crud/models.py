from django.db import models
from django.urls import reverse

class Category(models.Model):  # クラス名を大文字で始める
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name     = models.CharField(max_length=200)
    price    = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 'category' を大文字で修正
    img      = models.ImageField(blank=True, default='noImage.png')
    description  = models.TextField(blank=True, null=True)  # 商品詳細の説明フィールド  # デフォルト画像は適切か確認

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list')  # 商品リストに戻るためのURL
