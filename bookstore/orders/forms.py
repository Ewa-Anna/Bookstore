from django import forms


class OrderCreateForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    street = forms.CharField(max_length=255)
    apartment = forms.CharField(max_length=30)
    city = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=10)
    state = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
