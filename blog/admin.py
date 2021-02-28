from django.contrib import admin

# Register your models here.
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'title', 'description', 'published_on', 'is_published', 'is_featured')

    list_display_links = ('id', 'title',)

    list_editable = ('is_published', 'is_featured')


class CommentModelAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'user', 'blog', 'comment', 'comment_time')
    list_display_links = ('id', 'user')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentModelAdmin)