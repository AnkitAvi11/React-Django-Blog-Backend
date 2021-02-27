from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('auth/login/', views.login_user, name='login_user'),
    path('auth/get_user/', views.get_user, name='get_user'),
    path('auth/disable/', views.disable_user_account, name='disable_user'),
    path('auth/enable/', views.enable_user_account, name='enable_user_account'),
    path('auth/signup/', views.signup_user, name='signup'),
    path('auth/validate/', views.validate_user, name='validate_user_auth_state'),
    path('auth/get_user/<int:user_id>/', views.get_blog_user, name='getbloguser'),
    #   password reset views
    
]