from django.contrib import admin
from profiles.models import ProfileStatus, ProfileModel
# Register your models here.


admin.site.register(ProfileModel)
admin.site.register(ProfileStatus)