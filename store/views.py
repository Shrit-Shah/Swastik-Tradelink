from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

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