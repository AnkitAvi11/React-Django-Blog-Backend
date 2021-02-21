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


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_blog(request) : 
    user = request.user
    title = request.POST.get('title')
    slug = slugify(title)

    i=0
    while Blog.objects.filter(slug=slug).exists() : 
        slug = slug+i
        i += 1

    cover_image = request.FILES.get('cover_image', None)

    body = request.POST.get('body')

    published_on = datetime.now()

    try : 
        blog = Blog.objects.create(
            user = user,
            title = title,
            slug = slug,
            cover_image = cover_image,
            body = body,
            published_on = published_on
        )    
        return Response({
            'success' : True
        })
    except Exception as e: 
        return Response({
            'error' : 'Blog could not be created'
        })


@api_view(['GET'])
def get_all_blogs(request) : 
    
    try : 
        blogs = Blog.objects.all().order_by('-published_on')
        return Response(BlogSerializer(blogs, many=True).data, status=200)
    except Blog.DoesNotExist : 
        return Response({
            'message' : 'No blogs found'
        })