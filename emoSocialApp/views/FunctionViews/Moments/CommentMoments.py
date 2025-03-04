from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers
from emoSocialApp.models import UserProfile, User, Friends, FriendsRequest, Moments,MomentsComment
from datetime import datetime


class CommentMomentsView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        token = request.data['Token']
        commentId = jwt_decode_handler(token=token)['user_id']
        commentId = User.objects.get(id=commentId)
        commentMomentId = request.data['commentMomentId']
        commentMomentId = Moments.objects.get(id=commentMomentId)
        commentContent = request.data['commentContent']
        MomentsComment.objects.create(momentId=commentMomentId, commentId=commentId, commentContent=commentContent)

        return Response({"code": "success"})


