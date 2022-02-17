from django.db import models
from django.contrib.auth.models import User

from v1.products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product_name = models.CharField(verbose_name='Product name', max_length=100)
    first_name = models.CharField(verbose_name='First name', max_length=100)
    last_name = models.CharField(verbose_name='Last name', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100)
    address = models.CharField(verbose_name='Address', max_length=100)
    zipcode = models.CharField(verbose_name='Zipcode', max_length=100)
    place = models.CharField(verbose_name='Place', max_length=100)
    phone = models.CharField(verbose_name='Phone', max_length=100)
    paid_amount = models.DecimalField(verbose_name='Paid amount', max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(verbose_name='Stripe token', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.product_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Quantity', default=1)

    def __str__(self) -> str:
        return self.id
