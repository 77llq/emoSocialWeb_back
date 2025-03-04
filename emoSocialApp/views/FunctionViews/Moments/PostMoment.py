from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers
from emoSocialApp.models import UserProfile, User, Friends, FriendsRequest, Moments
from datetime import datetime


def check_sensitive_words(text, sensitive_words):
    text = text.lower()
    for word in sensitive_words:
        if word in text and word != '':
            print("Error: Sensitive word found:", word)
            return 'true'
    return 'false'


with open('static/sensitive_words/words.txt', 'r', encoding='utf-8') as f:
    sensitive_words = [line.strip().lower() for line in f]


class PostMomentView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        email_info = request.data['data']['_value']
        token = email_info['token']
        postId = jwt_decode_handler(token=token)['user_id']
        postTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        postContent = email_info['post_content']
        postPic = email_info['post_pic']
        postVideo = email_info['post_video']
        postId = User.objects.get(id=postId)
        if check_sensitive_words(postContent, sensitive_words) == 'true':
            return Response({"code": "sensitive"})
        if postContent:
            Moments.objects.create(postId=postId, postTime=postTime, postContent=postContent, postPic=postPic,
                                   postVideo=postVideo)
            return Response({"code": "success"})
        else:
            return Response({"code": "error"})
