from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import Friends, UserProfile,FriendsRequest


class GetFriendsInfoView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        friends_info = []
        newFriends_request=''
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        if Friends.objects.filter(userId=user_id):
            data = Friends.objects.filter(userId=user_id)
            for item in data:
                id = item.friendId.id
                intimacy = Friends.objects.get(friendId_id=item.friendId).intimacy
                name = UserProfile.objects.get(id=item.friendId).name
                avatar = UserProfile.objects.get(id=item.friendId).avatar
                signature = UserProfile.objects.get(id=item.friendId).signature
                friends_info.append({
                    'friend_id': id,
                    'friend_name': name,
                    'friend_avatar': avatar,
                    'friend_signature': signature,
                    'intimacy': intimacy,
                })
        if Friends.objects.filter(friendId=user_id):
            data = Friends.objects.filter(friendId=user_id)
            for item in data:
                id = item.userId.id
                intimacy = Friends.objects.get(userId_id=item.friendId).intimacy
                name = UserProfile.objects.get(id=item.userId).name
                avatar = UserProfile.objects.get(id=item.userId).avatar
                signature = UserProfile.objects.get(id=item.userId).signature
                friends_info.append({
                    'friend_id': id,
                    'friend_name': name,
                    'friend_avatar': avatar,
                    'friend_signature': signature,
                    'intimacy': intimacy,
                })
        if FriendsRequest.objects.filter(receiveRequestId=user_id):
            data = FriendsRequest.objects.filter(receiveRequestId=user_id)
            newFriends_request = len(data)
        return Response({'friends_info': friends_info,'newFriends_request': newFriends_request})
