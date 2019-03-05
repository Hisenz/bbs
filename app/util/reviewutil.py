from app.models import Review, User, Post


def add_review(user_pk, post_pk, content):
    try:
        review = Review()
        review.user = User.objects.get(pk=user_pk)
        review.post = Post.objects.get(pk=post_pk)
        review.review = content
        review.save()
        return 1
    except:
        return 0