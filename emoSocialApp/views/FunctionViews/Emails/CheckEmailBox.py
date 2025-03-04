from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, User, Email


class CheckEmailBoxView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        user_id = User.objects.get(id=user_id)
        email_info = []
        if Email.objects.filter(receiveId=user_id):
            data = Email.objects.filter(receiveId=user_id)
            for item in data:
                email_id = item.id
                email_topic = item.emailTopic
                email_content = item.emailContent
                send_time = item.sendTime
                send_id = item.sendId
                send_name = UserProfile.objects.get(id=send_id).name
                email_info.append({
                    'send_name': send_name,
                    'send_time': send_time,
                    'email_id': email_id,
                    'email_topic': email_topic,
                    'email_content': email_content,
                })
            return Response({'email_info': email_info})
        else:
            return Response({'email_info':''})

