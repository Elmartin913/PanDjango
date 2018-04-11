from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.template.response import TemplateResponse

from .models import  Contact
from .forms import ContactForm
# Create your views here.

class StartView(View):
    def get(self, request):
        return TemplateResponse(request, 'index.html')


class ContactView(View):
    def get(self,request):
        form = ContactForm()
        return TemplateResponse(request, 'contact_form.html', {'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']

            new_contact = Contact.objects.create(
                subject=subject,
                message=message,
                name=name,
                email=email,
                mobile=mobile,
            )

        return HttpResponse('Wiadomosc wysłana')



class BoardView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'board.html', {'contacts': contacts})