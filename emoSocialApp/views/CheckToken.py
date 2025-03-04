from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.Serializers.CheckAccountSerializers import AccountSerializers


class CheckTokenView(ModelViewSet):
    permission_classes = []

    def checkToken(request):
        token = request.GET.get('token')
        print(token)
        return HttpResponse('123')
