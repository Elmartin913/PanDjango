"""pandjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from website.views import StartView, ContactView, BoardView
from accounts.views import signup, LogoutView, LogInView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartView.as_view(), name='index'),
    path('contact', ContactView.as_view(), name='contact'),
    path('board', BoardView.as_view(), name='board'),
    #acconts
    path('signup', signup, name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LogInView.as_view(), name='login'),
]
