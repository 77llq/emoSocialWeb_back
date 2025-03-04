from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, Fans


class GetFansInfoView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        follow_num = ''
        fans_num = ''
        if Fans.objects.filter(fansId=user_id):
            data = Fans.objects.filter(fansId=user_id)
            follow_num = len(data)
        if Fans.objects.filter(userId=user_id):
            data = Fans.objects.filter(userId=user_id)
            fans_num = len(data)
        return Response({'follow_num': follow_num, 'fans_num': fans_num})
