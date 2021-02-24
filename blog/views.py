from blog.models import Blog
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from django.utils.text import slugify
from datetime import datetime
from rest_framework.response import Response
from .serialiazers import BlogSerializer
import random, string

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 


"""
Function that deals with the creation of blogs
@params
user : user that creates the blog
title : title of the blog
description : description of the blog (optional)
slug : slug fiels to search for a blog
cover_pic : cover pic for the blog
body : content of the blog
"""
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_blog(request) : 
    user = request.user
    title = request.POST.get('title')
    description = request.POST.get('description', None)
    slug = slugify(title)

    while Blog.objects.filter(slug=slug).exists() : 
        slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4))

    cover_image = request.FILES.get('cover_image', None)

    body = request.POST.get('body')

    published_on = datetime.now()

    try : 
        blog = Blog.objects.create(
            user = user,
            title = title,
            slug = slug,
            description = description,
            cover_image = cover_image,
            body = body,
            published_on = published_on
        )    
        return Response({
            'success' : True
        })
    except Exception as e : 
        return Response({
            'error' : 'Blog could not be created'
        })


""" 
Function to get all the featured blogs from the database where cover_image is not null
"""
@api_view(['GET'])
def get_all_blogs(request) : 
    try : 
        blogs = Blog.objects.filter(user__is_active=True, is_featured=True).exclude(cover_image='').order_by('-published_on')
        
        return Response(BlogSerializer(blogs, many=True).data, status=200)
    except Blog.DoesNotExist : 
        return Response({
            'message' : 'No blogs found'
        })

