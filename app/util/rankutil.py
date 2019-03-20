from app.models import Post, Rank
import datetime


def update():
    posts = Post.objects.all()
    now = datetime.datetime.now()
    first = get_for_pk(1)
    if not first or (now - first.update_time.replace(tzinfo=None)).seconds/60 > 1:
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
    return (P + Rev*5 + Read*0.1)*1.0/pow(T+2, 1.8)


def get_for_pk(pk):
    try:
        return Rank.objects.get(pk=pk)
    except:
        return None