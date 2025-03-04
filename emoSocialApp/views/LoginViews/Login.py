from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from emoSocialApp.Serializers.LoginAccountSerializers import LoginAccountSerializer
from emoSocialApp.models import User
import hashlib


class LoginView(ModelViewSet):
    authentication_classes = []  # 登录认证
    permission_classes = []

    def create(self, request, *args, **kwargs):
        account_info = LoginAccountSerializer(data=request.data)
        h = hashlib.sha256()
        if account_info.is_valid():
            account = account_info.data['account']
            if User.objects.filter(account=account):
                password = account_info.data['password']
                h.update(bytes(password, encoding='utf-8'))
                pwd_result = h.hexdigest()
                if User.objects.get(account=account).password == pwd_result:
                    user = User.objects.filter(account=account).first()
                    refresh = RefreshToken.for_user(user)
                    refresh['id'] = user.id
                    access_token = str(refresh.access_token)
                    type = User.objects.get(account=account).type
                    return Response({'mes': 'LoginSuccess', 'access_token': access_token,'type':type})
                else:
                    return Response({'mes': 'WrongPassword'})
            else:
                return Response({'mes': 'NoAccount'})
        else:
            return Response({'mes': 'InputError'})
