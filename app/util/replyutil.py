from app.models import Reply, User, Review
from django.shortcuts import get_object_or_404, get_list_or_404


def add(user_pk, review_pk, content, to_reply=None):

    try:
        reply = Reply()
        reply.user = User.objects.get(pk=user_pk)
        review = Review.objects.get(pk=review_pk)
        reply.content = content
        if to_reply is not None:
            reply.to_reply = User.objects.get(pk=to_reply)
        reply.save()
        review.replys.add(reply)
        return True
    except Exception as e:
        print(e)
        return False


def get_for_review(review):
    return Reply.objects.filter(review=Review.objects.get(pk=review)).order_by('time')
