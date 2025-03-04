from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import Friends, UserProfile,Fans


class GetFollowingView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        fans_info = []
        if Fans.objects.filter(userId=user_id):
            data = Fans.objects.filter(userId=user_id)
            for item in data:
                id = item.fansId.id
                name = UserProfile.objects.get(id=item.fansId).name
                avatar = UserProfile.objects.get(id=item.fansId).avatar
                fans_info.append({
                    'fans_id': id,
                    'name': name,
                    'avatar': avatar,
                })
        return Response({'fans_info': fans_info})
