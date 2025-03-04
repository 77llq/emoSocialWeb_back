from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import Friends


class DeleteFriendsView(ModelViewSet):
    permission_classes = []

    def destroy(self, request, *args, **kwargs):
        delete_id = request.query_params.get('delete_id')
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        if Friends.objects.filter(friendId=delete_id, userId=user_id):
            Friends.objects.filter(friendId=delete_id, userId=user_id).delete()
        if Friends.objects.filter(userId=delete_id, friendId=user_id):
            Friends.objects.filter(userId=delete_id, friendId=user_id).delete()
        return Response({'code': 'success'})
