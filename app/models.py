from django.db import models


# Create your models here.
# 用户
def avatar(self, filename):
    return 'app/' + str(self.pk) + '/avatar/init.'+filename.split('.')[-1]


def image(self, filename):
    return "image/" + filename

class User(models.Model):
    password = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    gender = models.BooleanField(default=True)
    nickname = models.CharField(max_length=20, unique=True)
    avatar = models.ImageField(upload_to=avatar, default=None, null=True)
    description = models.TextField(null=True, default=None)


# 板块
class Plate(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False)
    create_user = models.ForeignKey(User, to_field='nickname', on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, default=True)
    audit = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False)
    create_user = models.ForeignKey(User, to_field='nickname', on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, default=None)

    def __str__(self):
        return self.name


# 评论
class Review(models.Model):
    review = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.review


# 帖子
class Post(models.Model):
    user = models.ForeignKey(User, to_field='nickname', on_delete=models.DO_NOTHING)
    headline = models.CharField(max_length=20)
    plate = models.ForeignKey(Plate, to_field='name', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(auto_now_add=True)
    last_change_time = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, default=None)
    give_a_like = models.IntegerField(default=0)
    text_choice = models.BooleanField(null=True)
    read_num = models.IntegerField(default=0)
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.headline


# 点赞
class GiveLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Image(models.Model):
    image = models.ImageField(upload_to=image)