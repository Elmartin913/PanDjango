from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse

from .forms import SignUpForm, LogInForm

# Create your views here.

from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('board')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('board')



class LogInView(View):
    def get(self, request):
        form = LogInForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LogInForm(request.POST)
        if form.is_valid():
            login2 = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(
                username=login2,
                password=password
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('board')
            else:
                return HttpResponse('Niepoprawne dane do logowania')
