from django.db import models
from rest_framework import serializers
from .models import Blog, Comment
from accounts.serializers import UserAuthenticationSerializer


class BlogSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Blog
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer) : 
    user = UserAuthenticationSerializer()
    class Meta : 
        model = Comment
        fields = (
            'id',
            'user',
            'blog',
            'comment',
            'comment_time'
        )