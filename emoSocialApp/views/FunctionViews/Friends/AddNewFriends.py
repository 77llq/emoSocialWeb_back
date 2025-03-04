from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, User


class AddNewFriendsView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        target_account = request.query_params.get('target_account')
        if User.objects.filter(account=target_account):
            target_account_id = User.objects.get(account=target_account).id
            target_account_info = UserProfile.objects.get(id=target_account_id)
            target_info = {
                'friend_signature': target_account_info.signature,
                'friend_avatar': target_account_info.avatar,
                'friend_name': target_account_info.name
            }
            return Response({'code': 'success', 'target_info': target_info})
        else:
            return Response({'code': 'error'})
