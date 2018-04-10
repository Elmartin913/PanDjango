from django.shortcuts import render

from django.views import View
from django.template.response import TemplateResponse
# Create your views here.

class StartView(View):
    def get(self, request):
        return TemplateResponse(request, 'index.html')