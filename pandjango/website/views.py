from django.shortcuts import render

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
        form = ContactForm
        return TemplateResponse(request, 'contact_form.html', {'form':form})

    def post(self, request):
        pass

class BoardView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'board.html', {'contacts': contacts})