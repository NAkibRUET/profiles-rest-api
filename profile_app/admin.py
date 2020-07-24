from django.contrib import admin
from profile_app import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
