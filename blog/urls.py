from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create/', views.create_blog, name='create-blog'),
]