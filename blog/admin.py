from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'title', 'description', 'published_on', 'is_published')

    list_display_links = ('id', 'title')

    list_editable = ('is_published',)

admin.site.register(Blog, BlogAdmin)