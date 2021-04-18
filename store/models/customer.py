from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=20)


    def register(self):
        self.save()

    def __str__(self):
        return self.firstname

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExistEmail(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    def isExistPhone(self):
        if Customer.objects.filter(phone=self.phone):
            return True

        return False

