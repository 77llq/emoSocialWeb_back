from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler

from emoSocialApp.models import UserProfile, User, Friends, FriendsRequest


class AddFriendsByIdView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        token = request.data['token']
        user_id = jwt_decode_handler(token=token)['user_id']
        user = User.objects.get(id=user_id)
        add_id = request.data['postId']
        target_friend = User.objects.get(id=add_id)
        if user_id == add_id:
            return Response({'code': 'self'})
        elif FriendsRequest.objects.filter(receiveRequestId=target_friend, sendRequestId=user):
            return Response({'code': 'repeat'})
        elif Friends.objects.filter(friendId=target_friend,userId=user) or Friends.objects.filter(userId=target_friend,friendId=user):
            return Response({'code': 'already'})
        else:
            FriendsRequest.objects.create(receiveRequestId=target_friend, sendRequestId=user)
            return Response({'code': 'success'})

