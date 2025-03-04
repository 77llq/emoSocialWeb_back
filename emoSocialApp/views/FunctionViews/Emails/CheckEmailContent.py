from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, User, FriendsRequest, Email


class CheckEmailContentView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        email_id = request.query_params.get('email_id')
        email_topic = Email.objects.get(id=email_id).emailTopic
        send_id = Email.objects.get(id=email_id).sendId
        send_email = UserProfile.objects.get(id=send_id).email
        send_name = UserProfile.objects.get(id=send_id).name
        send_time = Email.objects.get(id=email_id).sendTime
        email_content = Email.objects.get(id=email_id).emailContent
        receive_id = Email.objects.get(id=email_id).receiveId
        receive_name = UserProfile.objects.get(id=receive_id).name
        receive_email = UserProfile.objects.get(id=receive_id).email
        email_info = {
            'email_topic': email_topic,
            'send_name': send_name,
            'send_email': send_email,
            'send_time': send_time,
            'receive_name': receive_name,
            'email_content': email_content,
            'receive_email': receive_email
        }
        return Response({'email_info': email_info})
