from django.contrib import admin
from user.models import *


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
class PostAdmin(admin.ModelAdmin):
    pass


#
@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    pass


#
@admin.register(Review)
class PostAdmin(admin.ModelAdmin):
    pass

