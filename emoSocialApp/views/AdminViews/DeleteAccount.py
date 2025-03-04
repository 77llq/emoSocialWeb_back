from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import Fans, User


class DeleteAccountView(ModelViewSet):
    permission_classes = []

    def destroy(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        id = User.objects.get(id=id)
        User.objects.get(id=id).delete()

        return Response({'code': 'success'})
