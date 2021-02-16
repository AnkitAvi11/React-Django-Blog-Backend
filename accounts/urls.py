from django.urls import path, re_path

from . import views

urlpatterns = [
    path('auth/login/', views.login_user, name='login_user'),
    path('auth/get_user/', views.get_user, name='get_user'),
]