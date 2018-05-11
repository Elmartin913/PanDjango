from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import reverse
from django.utils.html import mark_safe

from markdown import markdown
=======
>>>>>>> parent of d94c372... New Post View
=======
>>>>>>> parent of d94c372... New Post View

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, verbose_name='Tytuł')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Autor')
    body = models.TextField(verbose_name='Treść')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Data publikacji')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posty'

    def __str__(self):
<<<<<<< HEAD
<<<<<<< HEAD
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.publish.year,
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.publish.slug,
        ])

    def get_body_as_markdown(self):
        return mark_safe(markdown(self.body, safe_mode='escape'))
=======
        return self.title
>>>>>>> parent of d94c372... New Post View
=======
        return self.title
>>>>>>> parent of d94c372... New Post View
