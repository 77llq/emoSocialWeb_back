from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import FriendsRequest


class RejectNewFriendsView(ModelViewSet):
    permission_classes = []

    def destroy(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        apply_id = request.query_params.get('apply_id')
        user_id = user_id = jwt_decode_handler(token=token)['user_id']
        FriendsRequest.objects.filter(sendRequestId=apply_id, receiveRequestId=user_id).delete()
        return Response('deleted')
