from django.db import models

# Create your models here.
class Product(models.Model):
     name = models.CharField(max_length=200)
     price = models.PositiveIntegerField()
     maker = models.CharField(max_length=255, default="Unknown")

     class Meta:
          db_table = 'product'