from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import User, Moments, MomentsLike


class LikeMomentsView(ModelViewSet):
    permission_classes = []

    def create(self, request, *args, **kwargs):
        token = request.data['token']
        user_id = User.objects.get(id=jwt_decode_handler(token=token)['user_id'])
        momentId = Moments.objects.get(id=request.data['momentId'])
        if MomentsLike.objects.filter(momentId=momentId,likeId=user_id):
            MomentsLike.objects.filter(momentId=momentId, likeId=user_id).delete()
            return Response({"code": "error"})
        else:
            MomentsLike.objects.create(momentId=momentId,likeId=user_id)
            return Response({"code": "success"})



