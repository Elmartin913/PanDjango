from django.contrib import admin

from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish','status']
    list_filter = ('status', 'created', 'publish', 'author')
    ordering = ['status', 'publish']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    raw_id_fields = ('author',)


admin.site.register(Post, PostAdmin)