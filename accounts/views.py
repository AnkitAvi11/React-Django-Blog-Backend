from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, exceptions
from .serializers import UserAuthenticationSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

#   function to handle the login process and returning the auth token of the user
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
            
            return Response({
                "user" : UserAuthenticationSerializer(user).data,
                "token" : token.key
            })
    else : 
        return JsonResponse({
            'error' : 'Method type incorrect',
            'message' : 'Only POST method supported'
        })


#   function to get user information
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


#   function to disable the user account (to deactivate a user account temporarily)
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


#   function to activate back the user account which was already disabled (deactivated)
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