from django.db import models

from .categoery import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    company = models.CharField(max_length=30)
    description = models.CharField(max_length=400, default='')
    image = models.ImageField(upload_to='products_img/')
