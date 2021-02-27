from accounts.validators import is_email
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import UserAuthenticationSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
from .serializers import UserProfile

"""
Function to handle user registeration
@params : 
username : username of the user
fname : full name of the user
email : email address of the user
password : password of the user (stored in encrypted form)
"""
@api_view(['POST'])
def signup_user(request) : 
    if request.method == 'POST' : 
        fname = request.POST.get('fname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        fname = fname.split(' ', 2)
        if len(fname) >= 2 : 
            last_name = fname[1]
        else : 
            last_name = ''

        try : 

            #   validating email address and username
            if not is_email(email) : 
                return Response({
                    'message' : 'Enter a valid email address'
                })

            if User.objects.filter(Q(username = username) | Q(email=email)).exists() : 
                return Response({
                    'message' : 'User with those credentials already exists'
                })

            user = User.objects.create_user(
                username = username,
                first_name = fname[0],
                last_name = last_name,
                email = email,
                password = password
            )
            return Response({
                'user' : UserAuthenticationSerializer(user).data
            }, status=200)
        except : 
            return Response({
                'message' : 'User creation failed.'
            })

    else : 
        return Response({
            'message' : 'Invalid method (only POST method accepted)'
        })

"""
Function to handle the login process
Login authentication using username or email address both
@params : 
username : username of the user
email : email address as given by the user during registeration
password : password of the user as submitted during registeration
"""
@api_view(['POST'])
def login_user(request) : 
    if request.method == 'POST' : 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        #   validating the user 
        if user is None : 
            #   when the user is not authenticated
            return JsonResponse({
                'message' : 'Invalid username or password'
            })

        else : 
            #   when the user is authenticated
            token, created = Token.objects.get_or_create(
                user = user
            )

            if not user.is_active : 
                return Response({
                    'error' : 'Account Disabled',
                    'message' : 'Account has been disabled'
                })
            
            login(request, user)    #   login the user in
            return Response({
                "user" : UserAuthenticationSerializer(user).data,
                "token" : token.key
            })
    else : 
        return JsonResponse({
            'error' : 'Method type incorrect',
            'message' : 'Only POST method supported'
        })


"""
Function to get the user details
@params
username = username of the user whose details are to be searched
"""
@api_view(['GET'])
def get_user(request) : 
    username = request.GET.get('username')
    try : 
        user = User.objects.get(
            username = username
        )

        if not user.is_active : 
            return Response({
                    'error' : 'Account Disabled',
                    'message' : 'Account has been disabled'
                })

        return Response(UserAuthenticationSerializer(user).data)

    except User.DoesNotExist : 
        return Response({
            'error' : 'User does not exist.'
        })

    except Exception as e : 
        return Response({
            'error' : 'Some unknown error occurred'
        })


"""
Function to disable a user account
@params
authentication = admin authentication required
permission classes = IsAuthenticated and IsAdminUser
username = username of the user to be disabled
"""
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def disable_user_account(request) : 

    if request.method == 'POST' : 

        username = request.POST.get('username')

        try : 

            user = User.objects.get(username = username)
            user.is_active = False
            user.save()

            return Response({
                'message' : 'User account has been disabled'
            })

        except User.DoesNotExist : 

            return Response({
                'error' : 'User does not exist'
            })


"""
Function to enable the user account which was disabled earlier
@params
authentication = admin authentication required
permission classes = IsAuthenticated and IsAdminUser
username = username of the user which was disabled
"""
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def enable_user_account(request) : 

    if request.method == 'POST' : 

        username = request.POST.get('username')

        try : 

            user = User.objects.get(username = username)
            user.is_active = True
            user.save()

            return Response({
                'message' : 'User account has been activated successfully'
            })

        except User.DoesNotExist : 

            return Response({
                'error' : 'User does not exist'
            })


#   function to validate the login state of the user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def validate_user(request) : 
    user = request.user
    if user is None : 
        return Response({
            'error' : 'User is not authenticated'
        })

    else : 
        return Response({
            'user' : UserAuthenticationSerializer(user).data
        }, status=200)



@api_view(['GET'])
def get_blog_user(request, user_id) : 
    try : 
        user = User.objects.get(id = user_id)
        return Response(
            UserAuthenticationSerializer(user).data
        )
    except User.DoesNotExist : 
        return Response({
            'error' : 'user does not exist'
        },status=404)