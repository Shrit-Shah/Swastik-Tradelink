from django.shortcuts import render
from store.models.product import Product

def product(request, id):
    # Fetching the product using id
    product = Product.objects.filter(id=id)
    return render(request, 'product.html', {'product' : product[0]})