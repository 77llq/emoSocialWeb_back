from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers, AccountProfileSerializers
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import User, Moments, MomentsLike, UserProfile, Board
from datetime import datetime


class PostBoardView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        token = request.data['token']
        user_id = User.objects.get(id=jwt_decode_handler(token=token)['user_id'])
        post_name = UserProfile.objects.get(id=user_id).name
        board_topic = request.data['board']['board_topic']
        board_content = request.data['board']['board_content']
        postTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Board.objects.create(postId=user_id, postTopic=board_topic, postContent=board_content, postTime=postTime)
        return Response({"code": "success"})
