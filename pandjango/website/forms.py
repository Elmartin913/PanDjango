from django import forms
from django.core.validators import validate_email
from .validators import phone_validator


from .models import Contact, Sms

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': '*Imie'}),
        max_length=128,
        required=True,
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': '*Email'}),
        max_length=128,
        validators = [validate_email],
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': '*Wiadomość'}),
        max_length=1024,
        required=True,
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'type': 'number', 'placeholder': 'Telefon'}),
        validators=[phone_validator],
        required=False,
    )
    class Meta:
        model = Contact
        fields = [ 'name', 'email', 'mobile', 'message']


class SmsForm(forms.ModelForm):
    CHOICE = (
        (1, 'Mam nie typową propozycje. Proszę o kontakt.'),
        (2, 'Chcę unowocześnić moją firmę.'),
        (3, 'Ma pomysł na start-up.'),
        (4, 'Potrzebuję strony internetowej.'),
        (5, 'Chcę przeprzowadzić akcję promocyjną.'),
        (6, 'Potrzebuję kampanii marketingowej.'),
        (7, 'Chcę reaktywować moją listę mailingową.'),
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'placeholder': '*Imie'}),
        max_length=128,
        required=True,
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'rows': 1, 'type': 'number', 'placeholder': 'Telefon'}),
        validators=[phone_validator],
        required=False,
    )
    body = forms.ChoiceField(
        choices=Sms.CHOICE,
    )
    class Meta:
        model = Sms
        fields = ['name','mobile', 'body']