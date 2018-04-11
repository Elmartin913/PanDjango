from django import forms
from django.core.validators import EmailValidator

from .models import Contact

class ContactForm(forms.ModelForm):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': 'Temat'}),
        max_length=256,
        required=False,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': '*Wiadomość'}),
        max_length=1024,
        required=True,
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': 'Nadawca'}),
        max_length=128,
        required=False,
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': '*Email'}),
        max_length=128,
        validators = [EmailValidator()],
        required=True,
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'type': 'number', 'placeholder': 'Telefon'}),
        max_length=32,
        required=False,
    )
    class Meta:

        model = Contact
        fields = ['subject', 'message','name', 'email', 'mobile']
