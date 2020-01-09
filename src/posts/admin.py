from django.contrib import admin

# Register your models here.
from .models import Post, LostPost, FoundPost

admin.site.register(Post)
admin.site.register(LostPost)
admin.site.register(FoundPost)