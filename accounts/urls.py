from django.urls import path, re_path

from . import views

urlpatterns = [
    path('auth/login/', views.login_user, name='login_user'),
    path('auth/get_user/', views.get_user, name='get_user'),
    path('auth/disable/', views.disable_user_account, name='disable_user'),
    path('auth/enable/', views.enable_user_account, name='enable_user_account'),
]