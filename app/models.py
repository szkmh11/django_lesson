from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
     name = models.CharField(max_length=200)
     price = models.PositiveIntegerField()
          
# 新規作成・編集完了時のリダイレクト先
def get_absolute_url(self):
     return reverse('product_list')

#新規作成フォームを作ろうの章を関数で