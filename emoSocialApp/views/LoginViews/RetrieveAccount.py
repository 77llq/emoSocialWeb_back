from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.Serializers.SendCodeSerializers import AccountCheckSerializer, CodeCheckSerializer
from django.core.mail import send_mail
from emoSocialApp.models import User, UserProfile
import random
import string
import hashlib


def send_email(random_code, email_address):
    # 邮件主题
    subject = "EmoSocialApp 找回密码"
    # 邮件内容
    message = "您的验证码为:" + random_code
    # 发件人
    from_email = "2785118462@qq.com"
    # 收件人，可以是多个，以列表的形式存储
    recipient_list = [email_address]
    send_mail(subject=subject, from_email=from_email, recipient_list=recipient_list, message=message)
    return HttpResponse("Send email success")


def generate_code(length=5):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


class RetrieveAccountView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        retrieve_account = AccountCheckSerializer(data=request.data)
        if retrieve_account.is_valid():
            retrieve_account = retrieve_account.data['retrieve_account']
            if User.objects.filter(account=retrieve_account):
                userId = User.objects.get(account=retrieve_account).id
                userEmail = UserProfile.objects.get(id=userId).email
                random_code = generate_code()
                request.session["code"] = random_code
                send_email(random_code, userEmail)
                return Response('success')
            else:
                return Response('error!')
        else:
            return HttpResponse(retrieve_account.errors)

    def update(self, request, *args, **kwargs):
        h = hashlib.sha256()
        correct_code = request.session.get("code")
        data = CodeCheckSerializer(data=request.data)
        if data.is_valid():
            user_code = data.data['retrieve_confirm_code']
            if user_code == correct_code:
                account = data.data['retrieve_account']
                new_password = data.data['retrieve_password']
                h.update(bytes(new_password, encoding='utf-8'))
                pwd_result = h.hexdigest()
                User.objects.filter(account=account).update(password=pwd_result)
                return Response('success')
            else:
                return Response('error')
        else:
            return Response('error')
