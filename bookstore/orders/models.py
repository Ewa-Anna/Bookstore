from django.db import models
from book.models import Book


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    street = models.CharField(max_length=255, blank=True, verbose_name="Street Address")
    apartment = models.CharField(
        max_length=30, blank=True, verbose_name="Apartment Number"
    )
    city = models.CharField(max_length=100, blank=True, verbose_name="City")
    postal_code = models.CharField(
        max_length=10, blank=True, verbose_name="Postal Code"
    )
    state = models.CharField(max_length=100, blank=True, verbose_name="State")
    country = models.CharField(max_length=100, blank=True, verbose_name="Country")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return f"Order no {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
