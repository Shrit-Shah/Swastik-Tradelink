from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
import re
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        firstname = postData.get('firstname')
        lastname = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        repassword = postData.get('repassword')
        phone = postData.get('phone')

        # Validation
        value = {'firstname': firstname, 'lastname': lastname, 'email': email, 'phone': phone}

        error_msg = None
        customer = Customer(firstname=firstname,
                            lastname=lastname,
                            email=email,
                            password=password,
                            phone=phone)

        error_msg = self.validateCustomer(customer, repassword)

        # Saving
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {'error': error_msg, 'values': value}
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer, repassword):
        error_msg = None

        if not customer.firstname:
            error_msg = "First Name is Required!"
        elif len(customer.firstname) < 3:
            error_msg = "First Name must be 3 characters long!"
        elif not customer.lastname:
            error_msg = "Last Name is Required!"
        elif len(customer.lastname) < 3:
            error_msg = "Last Name must be 3 characters long!"
        elif not customer.phone:
            error_msg = "Phone No. is Required!"
        elif (len(customer.phone) < 10 or len(customer.phone) > 10):
            error_msg = "Phone No. must be a 10 digit number!"
        elif not customer.email:
            error_msg = "Email Address is Required!"
        elif customer.email:
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if not (re.search(regex, customer.email)):
                error_msg = "Invalid Email!"
        if not customer.password:
            error_msg = "Password is Required!"
        elif len(customer.password) < 8:
            error_msg = "Password must be 8 characters long!"
        elif customer.isExistEmail():
            error_msg = "User with this Email is already Registered!"
        elif customer.isExistPhone():
            error_msg = "User with this Phone No. is already Registered!"
        elif not repassword:
            error_msg = "Re-type the password!"
        elif repassword:
            if customer.password:
                if len(customer.password) != len(repassword):
                    error_msg = "Re-type the correct password!"
                for i in range(len(customer.password)):
                    if customer.password[i] != repassword[i]:
                        error_msg = "Re-type the correct password!"
                        break
            else:
                error_msg = "Password is Required!"

        return error_msg