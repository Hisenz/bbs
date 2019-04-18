from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('posts-list', request=request, format=format),
        'ranks': reverse('ranks-list', request=request, format=format),
        'recommended': reverse('recommended-list', request=request, format=format),
    })