from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("name", "email", "rating", "body")


class SearchForm(forms.Form):
    query = forms.CharField()
