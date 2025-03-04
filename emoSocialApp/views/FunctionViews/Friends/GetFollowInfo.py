from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import Friends, UserProfile, FriendsRequest, Fans


class GetFollowView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        user_info = []
        if Fans.objects.filter(fansId=user_id):
            data = Fans.objects.filter(fansId=user_id)
        if Fans.objects.filter(fansId=user_id):
            data = Fans.objects.filter(fansId=user_id)
            for item in data:
                id = item.userId.id
                name = UserProfile.objects.get(id=item.userId).name
                avatar = UserProfile.objects.get(id=item.userId).avatar
                user_info.append({
                    'user_id': id,
                    'name': name,
                    'avatar': avatar,
                })
        return Response({'user_info': user_info})

