from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers, AccountProfileSerializers
from emoSocialApp.models import User
import hashlib


class AccountView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        h = hashlib.sha256()
        account_info = AccountSerializers(data=request.data)
        profile_info = AccountProfileSerializers(data=request.data)
        if account_info.is_valid():
            password = account_info.data['password']
            h.update(bytes(password, encoding='utf-8'))
            pwd_result = h.hexdigest()
            account_instance = User.objects.create(**account_info.validated_data)
            account_instance.password = pwd_result
            account_instance.save()
            if profile_info.is_valid():
                profile_info.save()
            return Response("success")
        else:
            return Response(account_info.errors)
