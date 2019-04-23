from app.models import Post, Rank
import datetime


def update():
    """
    更新 首页的推荐
    posts 帖子的数据集
    now 当前时间

    :return:
    """
    posts = Post.objects.all()
    now = datetime.datetime.now()
    for post in posts:
        rank = get(post)
        post_time = post.create_time.replace(tzinfo=None)
        if rank:
            if (now - post_time).seconds/60 > 1:
                T = (now - post_time).seconds/60
                rank.rank = get_rank(post.give_a_like, post.reviews.count(), post.read_num, T)
                rank.save()
        else:
            rank = Rank()
            rank.post = post
            T = (now - post_time).seconds /60
            rank.rank = get_rank(post.give_a_like, post.reviews.count(), post.read_num, T)
            rank.save()


def get(post):
    try:
        return Rank.objects.get(post=post)
    except:
        return None


def get_rank(P, Rev, Read, T):
    """
    计算 Hack News 值
    :param P: 点赞数
    :param Rev: 评论数
    :param Read: 阅读数
    :param T: 时间差（以小时计算)
    :return: 通过hack news算法计算其值
    """
    return (P + Rev*5 + Read*0.1)*1.0/pow(T+2, 1.8)


def get_for_pk(pk):
    try:
        return Rank.objects.get(pk=pk)
    except:
        return None