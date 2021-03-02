from django.shortcuts import render
from .models.product import Product

def index(request):
    products = Product.get_all_products();
    return render(request, 'index.html', {'products' : products})

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')