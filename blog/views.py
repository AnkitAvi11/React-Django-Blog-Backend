from blog.models import Blog, Comment
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from django.utils.text import slugify
from datetime import datetime
from rest_framework.response import Response
from .serialiazers import BlogSerializer, CommentSerializer
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
FEATURED BLOGS
Function to get all the featured blogs from the database where cover_image is not null
"""
@api_view(['GET'])
def get_all_blogs(request) : 
    try : 

        #   trying to get all the blogs
        blogs = Blog.objects.filter(user__is_active=True, is_featured=True).exclude(cover_image='').order_by('-published_on')[:3]
        
        return Response(BlogSerializer(blogs, many=True).data, status=200)

    #   when the exception occurs of bloggin not existing anymore
    except Blog.DoesNotExist : 
        return Response({
            'message' : 'No blogs found'
        })


#   function to get individual blog using the blog slug
@api_view(['GET'])
def get_blog(request, blog_slug) : 
    try : 
        blog = Blog.objects.get(slug = blog_slug)
        return Response(
            BlogSerializer(blog, many=False).data
        )
    except Blog.DoesNotExist : 
        return Response({
            'error' : 'Blog was not found'
        }, status=404)


#   function to get the comments on a blog from the users
@api_view(['GET'])
def get_comments(request, blog_id) : 
    try : 
        comment = Comment.objects.filter(
            blog = blog_id
        ).order_by('-comment_time')

        return Response(CommentSerializer(comment, many=True).data, status=200)
        
    except Comment.DoesNotExist : 
        return Response({
            'error' : 'No comments were found'
        })


#   function to post comment on a blog post

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def createComment(request) : 
    blog_id = request.POST.get('blog_id')
    user = request.user
    comment = request.POST.get('comment')

    if comment is None : 
        return Response({
            'error' : 'Can not submit an empty comment'
        })
    

    #   handling the uncertain errors dure to server
    try : 

        #   creating the comment sent by the user on a blog
        Comment.objects.create(
            blog_id = blog_id,
            user = user
        )
    
    except Exception as e : 
        e.with_traceback()
        return Response({
            'error' : 'Some error occurred due to some technical errors'
        })
    

