from django.contrib import admin
from .models import UserProfile, Schedule, Review

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Schedule)
admin.site.register(Review)
