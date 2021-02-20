from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf.urls.static import static
from django.conf import settings

@api_view(['GET'])
def home_page(request) : 
    return Response({
        'message' : 'Hello World from django rest framework!'
    }, status=200)

#   url patterns of the entire project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    #   blog url configuration
    path('api/blog/', include('blog.urls'))
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

