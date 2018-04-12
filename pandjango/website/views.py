from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']

            new_contact = Contact.objects.create(
                message=message,
                name=name,
                email=email,
                mobile=mobile,
            )

        return HttpResponseRedirect('contact')



class BoardView(View):
    def get(self, request):
        contacts = Contact.objects.all().order_by('-id')
        return render(request, 'board.html', {'contacts': contacts})