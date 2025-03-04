from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, User, Email
from datetime import datetime

class SendEmailView(ModelViewSet):
    permission_classes = []

    def time_trans(self):
        now = datetime.now()
        # 格式化成指定格式
        formatted_date = now.strftime("%Y年%m月%d日 (%A) %p%I : %M")
        # 星期转换为中文
        weekday_mapping = {
            'Monday': '星期一',
            'Tuesday': '星期二',
            'Wednesday': '星期三',
            'Thursday': '星期四',
            'Friday': '星期五',
            'Saturday': '星期六',
            'Sunday': '星期日'
        }
        formatted_date = formatted_date.replace(now.strftime("%A"), weekday_mapping[now.strftime("%A")])
        # 下午/上午转换为中文
        formatted_date = formatted_date.replace("AM", "上午")
        formatted_date = formatted_date.replace("PM", "下午")
        return formatted_date

    def create(self, request, *args, **kwargs):
        email_info = request.data['email_info']['_value']
        token = email_info['token']
        user_id = jwt_decode_handler(token=token)['user_id']
        receive_id = email_info['receive_id']
        receive_email = email_info['receive_email']
        email_topic = email_info['email_topic']
        email_content = email_info['email_content']
        sendId = User.objects.get(id=user_id)
        receiveId = User.objects.get(id=receive_id)
        send_time = self.time_trans()
        if UserProfile.objects.filter(email=receive_email):
            Email.objects.create(sendId=sendId, receiveId=receiveId, emailTopic=email_topic,sendTime=send_time ,emailContent=email_content)
            return Response({'code': 'success'})
        else:
            return Response({'code':'error'})
