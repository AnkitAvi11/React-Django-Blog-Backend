from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf.urls import handler404

@api_view(['GET'])
def home_page(request) : 
    return Response({
        'message' : 'Hello World from django rest framework!'
    }, status=200)

#   url patterns of the entire project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('', home_page, name='homepage'),
    #   blog url configuration
    path('api/blog/', include('blog.urls'))
]

#   custom 404 page 
def handle_404(request, exception) : 
    data = {}
    return render(request, '404.html', data)

#   assigning the custom 404 view to the 404 handler
handler404 = handle_404