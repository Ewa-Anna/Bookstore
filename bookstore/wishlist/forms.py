from django import forms


class EmailWishlist(forms.Form):
    name = forms.CharField(max_length=25, label="Your Name")
    email_from = forms.EmailField(label="Your Email")
    email_to = forms.EmailField(label="Recipient Email")
    comments = forms.CharField(
        required=False, widget=forms.Textarea, label="Additional Comments"
    )
