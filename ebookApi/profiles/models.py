from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=140, blank=True, null=True)
    city = models.CharField(max_length=140, blank=True, null=True)
    avatar = models.ImageField(max_length=140, blank=True, null=True)
  
    def __str__(self):
        return self.user.username

class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return self.user_profile
    
