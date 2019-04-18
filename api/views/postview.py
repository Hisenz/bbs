from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from app.models import *
from api.serializers import PostSerializer
from rest_framework import status, generics, viewsets


class PostSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all().order_by('-create_time')
    serializer_class = PostSerializer


class PostSetOrderForReview(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all().order_by("-reviews")
    serializer_class = PostSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-create_time')
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all().order_by('-create_time')
    serializer_class = PostSerializer
# Create your views here.
@api_view(['GET', ])
def post_list(request, format=None):
    if request.method == "GET":
        posts = Post.objects.all().order_by('-create_time')
        try:
            if request.GET.get('order'):
                posts = Post.objects.all().order_by("-reviews")
        except:
            pass
        try:
            num = request.GET.get('num')
            posts = posts[0:int(num)]
        except:
            pass
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", ])
def post_detail(request, pk, format=None):
    try:
        post = Post.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


