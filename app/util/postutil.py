from app.models import Post, Tag, User, Plate
from  . import userutil


USER_ONT_EXIST = -1
SAVE_SUCCESS = 1
SAVE_FAILURE = 0
HEADLINE_EMPTY = -2
DESCRIPTION_EMPTY = -3


def add(user_id, post):
    if user_id == "":
        return USER_ONT_EXIST
    if post['headline'] == '':
        return HEADLINE_EMPTY
    if post['description'] == '':
        return DESCRIPTION_EMPTY
    try:
        new_post = Post()
        new_post.headline = post['headline']
        new_post.plate = Plate.objects.get(name=post['plate'])
        new_post.description = post['description']
        new_post.user = User.objects.get(pk=user_id)
        new_post.save()
        if post['tag_list'] != '':
            for tag_name in post['tag_list'].split(','):
                new_post.tags.add(Tag.objects.get(name=tag_name))
        new_post.save()
        return SAVE_SUCCESS
    except Exception as e:
        print(e)
        return SAVE_FAILURE


def get_posts_for_plate(plate_pk):
    plate = Plate.objects.get(pk=int(plate_pk))
    posts = Post.objects.filter(plate=plate)
    return posts


def get(pk):
    try:
        return Post.objects.get(pk=pk)
    except Exception:
        return None


def get_posts_for_user(user, order='-create_time'):
    return Post.objects.filter(user=user).order_by(order)

