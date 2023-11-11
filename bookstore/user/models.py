from datetime import date

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Date of Birth"
    )
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    shipping_address = models.OneToOneField(
        "ShippingAddress",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="profile",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["user"])]

    def __str__(self):
        return f"{self.user.username}'s profile"

    def calculate_age(self):
        if self.date_of_birth:
            today = date.today()
            age = (
                today.year
                - self.date_of_birth.year
                - (
                    (today.month, today.day)
                    < (self.date_of_birth.month, self.date_of_birth.day)
                )
            )

            if today.month < self.date_of_birth.month or (
                today.month == self.date_of_birth.month
                and today.day < self.date_of_birth.day
            ):
                age -= 1

            birth_month = self.date_of_birth.month
            birth_day = self.date_of_birth.day

            if today.month < birth_month or (
                today.month == birth_month and today.day < birth_day
            ):
                birth_month -= 1

            if today.month < birth_month:
                months = (12 - birth_month) + today.month
            else:
                months = today.month - birth_month

            if today.day < birth_day:
                days_in_previous_month = (
                    today
                    - date(today.year, (today.month - 1 if today.month > 1 else 12), 1)
                ).days
                days = days_in_previous_month - birth_day + today.day
            else:
                days = today.day - birth_day

            return age, months, days

        return None, None, None


class ShippingAddress(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="shipping_addresses",
    )
    main = models.BooleanField(default=False, verbose_name="Main Shipping Address")
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

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["street"]),
            models.Index(fields=["city"]),
            models.Index(fields=["state"]),
            models.Index(fields=["country"]),
        ]

    def __str__(self):
        return f"{self.street} {self.apartment}, {self.postal_code} {self.city}, {self.state} {self.country}"
