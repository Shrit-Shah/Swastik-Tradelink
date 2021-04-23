from django.shortcuts import render, redirect
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request , 'cart.html' , {'products' : products} )

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        qty = cart.get(product)
        if qty > 0:
            cart[product] = qty - 1
            if qty == 1:
                del cart[product]

        request.session['cart'] = cart
        if cart == {}:
            return redirect('homepage')

        return redirect('cart')