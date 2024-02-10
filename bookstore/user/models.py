from datetime import date
from dateutil.relativedelta import relativedelta

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


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
            age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            birth_date = self.date_of_birth.replace(year=today.year)
            if birth_date > today:
                age -= 1
                birth_date -= relativedelta(years=1)

            delta = relativedelta(today, birth_date)
            months = delta.months
            days = delta.days

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
    street = models.CharField(
        max_length=255, verbose_name="Street Address", blank=False
    )
    apartment = models.CharField(
        max_length=30, verbose_name="Apartment Number", blank=False
    )
    city = models.CharField(max_length=100, verbose_name="City", blank=False)
    postal_code = models.CharField(
        max_length=10,
        verbose_name="Postal Code",
        validators=[
            RegexValidator(
                regex=r"^\d{2}-\d{3}$",
                message="Postal code must be in the 00-000 format",
            )
        ],
        blank=False,
    )
    state = models.CharField(max_length=100, blank=False, verbose_name="State")
    country = models.CharField(max_length=100, blank=False, verbose_name="Country")

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
        return (
            f"{self.street} "
            f"{self.apartment}, "
            f"{self.postal_code} {self.city}, "
            f"{self.state} {self.country}"
        )
