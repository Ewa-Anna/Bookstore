from django import forms
from django.contrib.auth.models import User
from .models import Profile, ShippingAddress


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords are not matching.")
        return cd["password2"]

    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This e-mail address is already occupied.")
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
    

    def clean_email(self):
        data = self.cleaned_data["email"]
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError("This e-mail address is already occupied.")
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {'date_of_birth': forms.DateInput(attrs={'type': 'date'})}


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ["street", "apartment", "city", "postal_code",
                  "state", "country"]
    
    def is_duplicate(self):
        street = self.cleaned_data.get("street")
        apartment = self.cleaned_data.get("apartment")
        city = self.cleaned_data.get("city")
        postal_code = self.cleaned_data.get("postal_code")
        state = self.cleaned_data.get("state")
        country = self.cleaned_data.get("country")

        existing_addresses = ShippingAddress.objects.filter(
            street=street,
            apartment=apartment,
            city=city,
            postal_code=postal_code,
            state=state,
            country=country
        )

        return existing_addresses.exists()
class ShippingAddressEditForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ["street", "apartment", "city", "postal_code",
                  "state", "country"]