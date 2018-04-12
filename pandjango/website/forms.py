from django import forms
from django.core.validators import EmailValidator

from .validators import email_validator

from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': '*Nadawca'}),
        max_length=128,
        required=True,
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': '*Email'}),
        max_length=128,
        validators = [email_validator,],
        required=True,

    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Wiadomość'}),
        max_length=1024,
        required=False,
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'type': 'number', 'placeholder': 'Telefon'}),
        min_length=6, max_length=9,
        required=False,
    )

    #class Meta:

#        model = Contact
 #       fields = [ 'name', 'email', 'mobile', 'message']
