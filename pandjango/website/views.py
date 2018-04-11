from django.shortcuts import render

from django.views import View
from django.template.response import TemplateResponse

from .models import  Contact
# Create your views here.

class StartView(View):
    def get(self, request):
        return TemplateResponse(request, 'index.html')


class ContactView(View):
    def get(self,request):
        return TemplateResponse(request, 'contact.html')

class BoardView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'board.html', {'contacts': contacts})