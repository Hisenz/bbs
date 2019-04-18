
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from app.models import Rank
from api.serializers import RankSerializer
from rest_framework import status,generics, viewsets


class RankSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rank.objects.all().order_by('-rank')
    serializer_class = RankSerializer


class RankList(generics.ListAPIView):
    queryset = Rank.objects.all().order_by('-rank')
    serializer_class = RankSerializer


class RankDetail(generics.RetrieveAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer


@api_view(['GET'], )
def rank_list(request, format=None):

    if request.method == "GET":
        ranks = Rank.objects.all().order_by('-rank')
        try:
            num = request.GET.get('num')
            ranks = ranks[0:int(num)]
        except:
            pass
        serializer = RankSerializer(ranks, many=True)
        return Response(serializer.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", ])
def reco_detail(request, pk, format=None):
    try:
        ranks = Rank.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = RankSerializer(ranks)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

