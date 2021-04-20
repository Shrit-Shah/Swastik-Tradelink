from django.shortcuts import render, redirect
from store.models.product import Product
from django.views import View

class Index(View):
    def get(self, request):
        products = Product.get_all_products()
        return render(request, 'index.html', {'products': products})

    def post(self, request):
        quantity = int(request.POST.get("quantity"))
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            qty = cart.get(product)
            if qty:
                cart[product] = qty+quantity
            else:
                cart[product] = quantity
        else:
            cart = {}
            cart[product] = quantity

        request.session['cart'] = cart

        return redirect('homepage')