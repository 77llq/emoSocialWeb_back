from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, Fans


class ProfileView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        user_info = {
            'name': UserProfile.objects.get(id=user_id).name,
            'email': UserProfile.objects.get(id=user_id).email,
            'gender': UserProfile.objects.get(id=user_id).gender,
            'birthday': UserProfile.objects.get(id=user_id).birthday,
            'avatar_url': UserProfile.objects.get(id=user_id).avatar,
            'signature': UserProfile.objects.get(id=user_id).signature,
            'profileBp': UserProfile.objects.get(id=user_id).profileBp,
            'id': user_id,
        }
        return Response(user_info)
