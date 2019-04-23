from rest_framework import viewsets
from api.serializers import ReplySerializer
from app.models import Reply


class ReplySet(viewsets.ModelViewSet):
    queryset = Reply.objects.all().order_by('time')
    serializer_class = ReplySerializer


