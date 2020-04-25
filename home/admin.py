from django.contrib import admin
from .models import Post, Profile #, Friend

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
# admin.site.register(Friend)