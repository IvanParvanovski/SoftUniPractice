from django.contrib import admin

from app.models.comment import Comment
from app.models.like import Like
from app.models.pet import Pet

admin.site.register(Pet)
admin.site.register(Like)
admin.site.register(Comment)

# Register your models here.
