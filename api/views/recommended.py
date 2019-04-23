
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from app.models import Recommended
from api.serializers import RecommendedSerializer
from rest_framework import status,generics, viewsets


class RecommendedSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recommended.objects.filter(is_true=True)
    serializer_class = RecommendedSerializer


class RecommendedList(generics.ListAPIView):
    queryset = Recommended.objects.filter(is_true=True)
    serializer_class = RecommendedSerializer


class RecommendedDetail(generics.RetrieveAPIView):
    queryset = Recommended.objects.filter(is_true=True)
    serializer_class = RecommendedSerializer

@api_view(['GET'], )
def recommended_list(request, format=None):

    if request.method == "GET":
        recommends = Recommended.objects.filter(is_true=True)
        try:
            num = request.GET.get('num')
            recommends = recommends[0:int(num)]
        except:
            pass
        serializer = RecommendedSerializer(recommends, many=True)
        return Response(serializer.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", ])
def recommended_detail(request, pk, format=None):
    try:
        recommends = Recommended.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = RecommendedSerializer(recommends)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

