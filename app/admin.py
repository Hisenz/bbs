from django.contrib import admin
from app.models import *


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


#
@admin.register(Plate)
class PostAdmin(admin.ModelAdmin):
    pass


#
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    pass


#
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


#
@admin.register(Review)
class PostAdmin(admin.ModelAdmin):
    pass

