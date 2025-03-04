from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, Fans, Board


class GetBoardContentView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        data = Board.objects.filter().last()
        boardForm = {
            'boardTopic': data.postTopic,
            'boardContent': data.postContent,
            'postTime': data.postTime,
        }
        return Response({'data': boardForm})
