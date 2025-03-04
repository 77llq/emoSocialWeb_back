from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.Serializers.CheckAccountSerializers import AccountSerializers


class CheckAccountView(ModelViewSet):
    permission_classes = []
    
    def create(self, request, *args, **kwargs):
        account_info = AccountSerializers(data=request.data)
        if account_info.is_valid():
            return Response("success")
        else:
            return Response(account_info.errors)
