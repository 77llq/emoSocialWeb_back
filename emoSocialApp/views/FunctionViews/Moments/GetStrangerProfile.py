from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, Fans, Moments


class GetStrangerProfileView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get('id')
        follow_num = ''
        fans_num = ''
        if Fans.objects.filter(fansId=user_id):
            data = Fans.objects.filter(fansId=user_id)
            follow_num = len(data)
        if Fans.objects.filter(userId=user_id):
            data = Fans.objects.filter(userId=user_id)
            fans_num = len(data)
        user_info = {
            'name': UserProfile.objects.get(id=user_id).name,
            'email': UserProfile.objects.get(id=user_id).email,
            'gender': UserProfile.objects.get(id=user_id).gender,
            'birthday': UserProfile.objects.get(id=user_id).birthday,
            'avatar_url': UserProfile.objects.get(id=user_id).avatar,
            'signature': UserProfile.objects.get(id=user_id).signature,
            'profileBp': UserProfile.objects.get(id=user_id).profileBp,
            'follow': follow_num,
            'following': fans_num,
            'id': user_id,
        }
        strangerMomentsInfo = []
        friend_moments = Moments.objects.filter(postId=user_id).order_by('-postTime')
        for item in friend_moments:
            moment_form = {
                           'postName': UserProfile.objects.get(id=item.postId).name,
                           'postAvatar': UserProfile.objects.get(id=item.postId).avatar,
                           'postContent': item.postContent,
            }
            strangerMomentsInfo.append(moment_form)
        return Response({'user_info': user_info,'strangerMomentsInfo': strangerMomentsInfo})
