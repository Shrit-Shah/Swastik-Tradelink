from django.shortcuts import render, redirect
from store.models.product import Product
from django.views import View

class Index(View):
    def get(self, request):
        products = Product.get_all_products()
        print('you are : ', request.session.get('customer_email'))
        return render(request, 'index.html', {'products': products})

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            qty = cart.get(product)
            if qty:
                cart[product] = qty+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')
