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

    #   overriding the save method
    def save(self, *args, **kwargs) : 
        try : 
            this = UserProfile.objects.get(id = self.id)
            if this.profile_pic != self.profile_pic and this.profile_pic != 'default.png' : 
                this.profile_pic.delete(save=False)
        except : 
            pass

        return super().save(*args, **kwargs)


#   creating a trigger to automatically create user profile
def create_user_signal(sender, **kwargs) : 
    if kwargs['created'] : 
        UserProfile.objects.create(user = kwargs['instance'])


#   connecting the trigger to the user model
post_save.connect(create_user_signal, User)

