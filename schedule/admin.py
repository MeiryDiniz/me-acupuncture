from django.contrib import admin
from .models import UserProfile, Schedule

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Schedule)
