from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=128, null=True, verbose_name='Nadawca')
    subject = models.CharField(max_length=255, blank=True, verbose_name='Temat')
    message = models.TextField(max_length=4000, verbose_name='Wiadomość')
    email = models.CharField(max_length=70,blank=True, verbose_name='Email')
    mobile = models.CharField(max_length=9, blank=True, null=True,default='000000000', verbose_name='Telefon')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Wiadomość'
        verbose_name_plural = 'Wiadomości'


    def __str__(self):
        return self.name


class Sms(models.Model):
    name = models.CharField(max_length=16, null=True, verbose_name='Imię')
    mobile = models.CharField(max_length=9, blank=True, null=True, verbose_name='Telefon')
    message = models.TextField(max_length=124, verbose_name='Wiadomość')
    created = models.DateTimeField(auto_now_add=True)
