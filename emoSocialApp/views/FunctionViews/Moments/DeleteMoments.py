from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import Fans, User,Moments


class DeleteMomentsView(ModelViewSet):
    permission_classes = []

    def destroy(self, request, *args, **kwargs):
        momentId = request.query_params.get('id')
        Moments.objects.filter(id=momentId).delete()
        return Response({'code': 'success'})
