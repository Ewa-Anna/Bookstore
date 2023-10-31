from django import forms

from user.models import ShippingAddress

from .models import Order


class OrderCreateForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    street = forms.CharField(max_length=255, required=False)
    apartment = forms.CharField(max_length=30, required=False)
    city = forms.CharField(max_length=100, required=False)
    postal_code = forms.CharField(max_length=10, required=False)
    state = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=100, required=False)
