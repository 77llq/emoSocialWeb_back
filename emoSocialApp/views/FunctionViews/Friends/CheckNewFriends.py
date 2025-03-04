from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, User, FriendsRequest


class CheckNewFriendsView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        request_info = []
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        if FriendsRequest.objects.filter(receiveRequestId=user_id):
            data = FriendsRequest.objects.filter(receiveRequestId=user_id)
            for item in data:
                request_avatar = UserProfile.objects.get(id=item.sendRequestId).avatar
                request_name = UserProfile.objects.get(id=item.sendRequestId).name
                request_signature = UserProfile.objects.get(id=item.sendRequestId).signature
                request_id = item.sendRequestId.id
                request_info.append({
                    'avatar': request_avatar,
                    'name': request_name,
                    'signature': request_signature,
                    'id': request_id
                })
            return Response({'request_info': request_info})
        else:
            return Response({'request_info': []})

