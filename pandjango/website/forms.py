from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    subject = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Temat'}),
        max_length=256,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Wiadomość'}),
        max_length=1024,
    )
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Nadawca'}),
        max_length=128,
    )
    email = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Email'}),
        max_length=128,
    )
    mobile = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Telefon'}),
        max_length=32,
    )
    class Meta:

        model = Contact
        fields = ['subject', 'message','name', 'email', 'mobile']
