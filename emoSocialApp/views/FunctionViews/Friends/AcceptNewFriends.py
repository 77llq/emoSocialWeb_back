from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers
from emoSocialApp.models import UserProfile, User, Friends, FriendsRequest


class AcceptNewFriendsView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        apply_id = request.data['apply_id']
        token = request.data['token']
        user_id = jwt_decode_handler(token=token)['user_id']
        user_id = User.objects.get(id=user_id)
        apply_id = User.objects.get(id=apply_id)
        Friends.objects.create(userId=user_id,friendId=apply_id)
        FriendsRequest.objects.filter(receiveRequestId=user_id,sendRequestId=apply_id).delete()
        return Response('123')
