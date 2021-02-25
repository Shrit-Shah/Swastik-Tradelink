from django.db import models

from .Scategory import SubCategory
from .category  import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    company = models.CharField(max_length=30)
    description = models.CharField(max_length=400, default='')
    image = models.ImageField(upload_to='products_img/')

    def __str__(self):
        return self.name



