from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.models import UserProfile, User, FriendsRequest, Email, Moments, MomentsLike
from emoSocialApp.Serializers.RegisterSerializers import AccountProfileSerializers, AccountSerializers


class GetAllMomentsView(ModelViewSet):
    permission_classes = []
    serializer_class = AccountSerializers

    def list(self, request, *args, **kwargs):
        allUsers = []
        data = Moments.objects.all()
        for item in sorted(data, key=lambda x: x.postId.id):
            likes = 0
            for item2 in MomentsLike.objects.all():
                if item.id == item2.momentId.id:
                    likes += 1
            obj = {
                'id': item.postId.id,
                'account': User.objects.get(id=item.postId).account,
                'avatar': UserProfile.objects.get(id=item.postId).avatar,
                'name': UserProfile.objects.get(id=item.postId).name,
                'content': item.postContent,
                'postTime': item.postTime,
                'video': item.postVideo,
                'pic': item.postPic,
                'likes': likes,
                'momentId': item.id
            }
            allUsers.append(obj)
        return Response({"data": allUsers})
