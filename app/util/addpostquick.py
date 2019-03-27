import random

from app.models import Post, User, Plate

post = Post()
post.headline = input()
post.plate = Plate.objects.get(name=input())
post.description = input()
post.user = User.objects.get(pk=random.choice([1, 2]))
post.save()