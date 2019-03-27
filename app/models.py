from django.db import models


# Create your models here.
# 用户
def avatar(self, filename):
    return 'app/' + str(self.pk) + '/avatar/init.'+filename.split('.')[-1]


def image(self, filename):
    return "post/image/" + filename


def postfile(self, filename):
    return  "post/attachment/"+ filename


class User(models.Model):
    password = models.CharField(max_length=40, verbose_name="密码")
    email = models.EmailField(unique=True, verbose_name="邮箱")
    gender = models.BooleanField(default=True, verbose_name="性别")
    nickname = models.CharField(max_length=20, unique=True, verbose_name="昵称")
    avatar = models.ImageField(upload_to=avatar, default=None, null=True, verbose_name="头像")
    description = models.TextField(null=True, default="", verbose_name="个人说明")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


# 板块
class Plate(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False, verbose_name="名称")
    create_user = models.ForeignKey(User, to_field='nickname', on_delete=models.DO_NOTHING, verbose_name="创建者")
    description = models.TextField(null=True, default=True, verbose_name="描述")
    audit = models.BooleanField(default=False, verbose_name="审核结果")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "板块"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False, verbose_name="名称")
    create_user = models.ForeignKey(User, to_field='nickname', on_delete=models.DO_NOTHING, verbose_name="创建者")
    description = models.TextField(null=True, default=None, verbose_name="描述")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 评论
class Review(models.Model):
    review = models.TextField(verbose_name="内容")
    time = models.DateTimeField(auto_now_add=True, verbose_name="时间")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="创建者")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.review


# 帖子
class Post(models.Model):
    user = models.ForeignKey(User, to_field='nickname', on_delete=models.DO_NOTHING, verbose_name="创建者")
    headline = models.CharField(max_length=20, verbose_name="标题")
    plate = models.ForeignKey(Plate, to_field='name', on_delete=models.CASCADE, verbose_name="所属板块")
    tags = models.ManyToManyField(Tag, verbose_name="包含标签")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_change_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    description = models.TextField(null=True, default=None, verbose_name="内容")
    give_a_like = models.IntegerField(default=0, verbose_name="点赞")
    read_num = models.IntegerField(default=0, verbose_name="阅读数")
    reviews = models.ManyToManyField(Review, verbose_name="评论")
    attachment = models.FileField(upload_to=postfile, null=True, verbose_name="附件")

    class Meta:
        verbose_name = "帖子"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.headline


# 点赞
class GiveLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


# 图片存放
class Image(models.Model):
    image = models.ImageField(upload_to=image)


# 帖子排行
class Rank(models.Model):
    rank = models.FloatField(default=0)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, verbose_name="帖子")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "排行榜"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pk