from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers, AccountProfileSerializers
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import User, Moments, MomentsLike, UserProfile, Board
from datetime import datetime


class CreateAdminAccountView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        dataForm = request.data['dataForm']
        dataForm['type'] = '管理员'
        newAdmin = AccountSerializers(data=dataForm)
        newAdminProfile = AccountProfileSerializers(data=dataForm)
        for item in User.objects.all():
            if dataForm['account'] == item.account:
                return Response({"code": "already"})
            else:
                if newAdmin.is_valid():
                    newAdmin.save()
                    if newAdminProfile.is_valid():
                        newAdminProfile.save()
                        return Response({"code": "success"})
                    else:
                        return Response({"code": "error"})
                else:
                    return Response({"code": "error"})
