from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("user", "rating", "body")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ReviewForm, self).__init__(*args, **kwargs)
    
        self.fields['user'].initial = user
        self.fields['user'].widget = forms.TextInput(attrs={'readonly': 'readonly', 'disabled': 'disabled'})

class SearchForm(forms.Form):
    query = forms.CharField()
