from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.Serializers.TokenSerializers import TokenSerializer
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import User, UserProfile
from emoSocialApp.Serializers.UpdateProfileSerializers import UpdateProfileSerializer


class EditProfileView(ModelViewSet):
    permission_classes = []

    def update(self, request, *args, **kwargs):
        update_info = UpdateProfileSerializer(data=request.data['account_info'])
        token = TokenSerializer(data=request.data)

        if update_info.is_valid():
            if token.is_valid():
                user_id = jwt_decode_handler(token=token.data['token'])['user_id']
                update_data = update_info.data
                print(update_data)
                UserProfile.objects.filter(id=user_id).update(name=update_data['name'])
                UserProfile.objects.filter(id=user_id).update(avatar=update_data['avatar_url'])
                UserProfile.objects.filter(id=user_id).update(profileBp=update_data['profileBp'])
                UserProfile.objects.filter(id=user_id).update(signature=update_data['signature'])
                UserProfile.objects.filter(id=user_id).update(gender=update_data['gender'])
                UserProfile.objects.filter(id=user_id).update(email=update_data['email'])
                UserProfile.objects.filter(id=user_id).update(birthday=update_data['birthday'])
                user_info = {
                    'name': UserProfile.objects.get(id=user_id).name,
                    'email': UserProfile.objects.get(id=user_id).email,
                    'gender': UserProfile.objects.get(id=user_id).gender,
                    'birthday': UserProfile.objects.get(id=user_id).birthday,
                    'avatar_url': UserProfile.objects.get(id=user_id).avatar,
                    'profileBp': UserProfile.objects.get(id=user_id).profileBp,
                    'signature': UserProfile.objects.get(id=user_id).signature,
                }
                return Response({'mes': 'success', 'user_info': user_info})
        else:
            return Response({'mes': 'error'})
