from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    img = models.ImageField(blank=True, default='noImage.png')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list')
