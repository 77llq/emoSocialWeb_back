from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.models import UserProfile, User, FriendsRequest, Email
from emoSocialApp.Serializers.RegisterSerializers import AccountProfileSerializers, AccountSerializers


class GetAllUsersView(ModelViewSet):
    permission_classes = []
    serializer_class = AccountSerializers

    def list(self, request, *args, **kwargs):
        allUsers = []
        data = User.objects.all()
        for item in data:
            obj = {
                'id': item.id,
                'account': item.account,
                'avatar':UserProfile.objects.get(id=item).avatar,
                'name': UserProfile.objects.get(id=item).name,
                'email': UserProfile.objects.get(id=item).email,
                'gender': UserProfile.objects.get(id=item).gender,
                'birthday': UserProfile.objects.get(id=item).birthday,
                'idNumber': User.objects.get(id=item).idNumber
            }
            allUsers.append(obj)
        return Response({"data": allUsers})
