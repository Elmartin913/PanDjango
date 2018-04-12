from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from .forms import SignUpForm

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
        return HttpResponseRedirect('index')