from app.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", 'nickname', 'gender', 'avatar')


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = ('id', 'name')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('review', 'time', 'user')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)
    plate = PlateSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('url', 'id', 'headline', 'description', 'user', 'plate', 'create_time', 'read_num', 'reviews')


class RankSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(view_name="post-detail", read_only=True)

    class Meta:
        model = Rank
        fields = ('url', 'id', 'rank', 'post')


class RecommendedSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(view_name="post-detail", read_only=True)

    class Meta:
        model = Recommended
        fields = ('url', 'id', 'cover', 'create_time', 'post')


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'review', 'time', 'user')


class ReplyNoToReplySerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = ('id', 'review', 'user', 'content', 'time')


class ReplySerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    to_reply = ReplyNoToReplySerializer(read_only=True)

    class Meta:
        model = Reply
        fields = ('id', 'review', 'to_reply', 'user', 'content', 'time')