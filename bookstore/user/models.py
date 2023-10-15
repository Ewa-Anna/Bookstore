from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    street = models.CharField(max_length=255, blank=True, verbose_name="Street Address")
    apartment = models.CharField(max_length=30, blank=True, verbose_name="Apartment Number")
    city = models.CharField(max_length=100, blank=True, verbose_name="City")
    postal_code = models.CharField(max_length=10, blank=True, verbose_name="Postal Code")
    state = models.CharField(max_length=100, blank=True, verbose_name="State")
    country = models.CharField(max_length=100, blank=True, verbose_name="Country")

    def __str__(self):
        return f"{self.user.username}'s profile"