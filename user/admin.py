from django.contrib import admin
from user.models import *

# Register your models here.

admin.register(User, Plate, Tag, Post, Review)