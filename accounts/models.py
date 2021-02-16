from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta
from django.db.models.signals import post_save


#   user profile model
class UserProfile(models.Model) : 
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True, null=True)

    profile_pic = models.ImageField(
        upload_to = 'profile/%Y/%m/',
        default = 'default.png'
    )

    dob = models.DateField(blank=True, null=True)
    joined_on = models.DateTimeField(default=datetime.now())

    def __str__(self) : 
        return self.user.username


#   creating a trigger to automatically create user profile
def create_user_signal(sender, **kwargs) : 
    if kwargs['created'] : 
        UserProfile.objects.create(user = kwargs['instance'])


#   connecting the trigger to the user model
post_save.connect(create_user_signal, User)

