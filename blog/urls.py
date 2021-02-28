from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create/', views.create_blog, name='create-blog'),
    path('all/', views.get_all_blogs, name='all_blogs'),
    path('<slug:blog_slug>/', views.get_blog, name='get_blog'),
    path('comment/<int:blog_id>/', views.get_comments, name='comments'),
]