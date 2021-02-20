from django.db import models
from django.contrib.auth.models import User
from datetime import  datetime, timedelta

# Create your models here.
class Blog(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)

    cover_image = models.ImageField(upload_to = 'blogs/%Y/%m/',default='None', blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    body = models.TextField()

    published_on = models.DateTimeField(
        default=datetime.now()
    )

    def __str__(self) : return self.title

    #   function to check if the blog is recently published or not
    # def is_recent(self) : 
    #     if self.published_on >= datetime.now() - timedelta(days=3) : 
    #         return True
    #     return False

    #   overriding the save method and delete method
    def save(self, *args, **kwargs) : 
        try : 
            this = Blog.objects.get(id = self.id)
            if this.cover_image != self.cover_image : # deletes the old cover image when a user updates the blog and uploads a new cover image just in case
                this.cover_image.delete(save=False)
        except : 
            pass

        return super().save(*args, **kwargs)

    #   overriding the delete method
    def delet(self, *args, **kwargs) : 
        self.cover_image.delete(save=False) #   deletes the cover image associated with the blog
        return super().delete(*args, **kwargs)