from django.contrib import admin

from .models.category import Category
from .models.Scategory import SubCategory
# from .models.categoery import Categoery, SubCategoery
from .models.product import Product

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)