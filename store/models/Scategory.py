from django.db import models

from .category import Category


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    subcategory = models.CharField(max_length=40)

    def __str__(self):
        return self.subcategory



