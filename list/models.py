from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Lists(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    done = models.BooleanField(default=False)
    
    
    def __str__(self):
        return  self.title + '-' + self.owner.username 
    