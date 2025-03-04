from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import Fans,User,Email


class DeleteEmailsView(ModelViewSet):
    permission_classes = []

    def destroy(self, request, *args, **kwargs):
        email_id = request.query_params.get('email_id')
        if Email.objects.filter(id=email_id):
            Email.objects.filter(id=email_id).delete()
            return Response({'code': 'success'})
        else:
            return Response({'code': 'error'})

