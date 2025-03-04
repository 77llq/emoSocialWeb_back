from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import Friends,Fans,User


class FollowView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        token = request.data['token']
        user_id = jwt_decode_handler(token=token)['user_id']
        follow_id = request.data['follow_id']
        follow_user = User.objects.get(id=follow_id)
        user = User.objects.get(id=user_id)
        if Fans.objects.filter(userId=follow_user, fansId=user):
            return Response({'code': 'already'})
        else:
            Fans.objects.create(userId=follow_user, fansId=user)
            return Response({'code': 'success'})
