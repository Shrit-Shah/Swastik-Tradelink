from django.contrib import admin

from .models.category import Category
from .models.Scategory import SubCategory
from .models.product import Product
from .models.customer import Customer

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Customer)
