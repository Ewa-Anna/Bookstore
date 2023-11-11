from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from book.models import Book


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return f"Order no {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_stripe_url(self):
        if not self.stripe_id:
            return ''
        if '_test_' in settings.STRIPE_SECRET_KEY:
            path = '/test/' # for testing
        else: 
            path = '/' # for production
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
