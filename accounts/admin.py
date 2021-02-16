from django.contrib import admin

from .models import UserProfile

class UserprofileAdmin(admin.ModelAdmin) : 
    list_display = (
        'id',
        'user',
        'bio',
        'joined_on',
        'dob'
    )
    list_display_links = ('id', 'user')
        

admin.site.register(UserProfile, UserprofileAdmin)
