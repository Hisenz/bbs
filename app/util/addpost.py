import random

from app.models import Post, User, Plate
import json


plates = {
    "arch": "架构",
    "avi": "音视频开发",
    "career": "程序人生",
    "cloud": "云计算/大数据",
    "db": "数据库",
    "engineering": "研发管理",
    "fund": "计算机基础",
    "game": "游戏开发",
    "iot": "物联网",
    "lang": "编程语言",
    "mobile": "移动开发",
    "ops": "运维",
    "other": "其他",
    "sec": "安全",
    "web": "前端",
}
USER_CHOICE = [1, 2, 3, 4]
with open('posts.json', encoding="utf-8") as f:
    posts = json.load(f)
    for key, value in posts.items():
        plate = Plate.objects.get(name=plates[key])
        for num, postdata in posts[key].items():
            try:
                post = Post()
                post.headline = postdata['headline']
                post.description = postdata['content']
                post.plate = plate
                post.user = User.objects.get(pk=random.choice(USER_CHOICE))
                post.save()
            except:
                pass