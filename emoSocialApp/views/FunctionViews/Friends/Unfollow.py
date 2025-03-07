from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import Fans,User


class UnfollowView(ModelViewSet):
    permission_classes = []

    def destroy(self, request, *args, **kwargs):
        token = request.data['token']
        user_id = jwt_decode_handler(token=token)['user_id']
        unfollow_id = request.query_params.get('unfollow_id')
        unfollow_user = User.objects.get(id=unfollow_id)
        user = User.objects.get(id=user_id)
        if Fans.objects.filter(userId=unfollow_user, fansId=user):
            Fans.objects.filter(userId=unfollow_user, fansId=user).delete()
            return Response({'code': 'success'})
        else:
            return Response({'code': 'not_your_follow'})

