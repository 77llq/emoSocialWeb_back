from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from emoSocialApp.models import UserProfile, Fans, Board,User


class GetRecommendUsersView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        allUsers = []
        token = request.query_params.get('token')
        user_id = jwt_decode_handler(token=token)['user_id']
        allInfo = UserProfile.objects.all()

        for item in allInfo:
            if item.id.id != user_id and User.objects.get(id=item.id).type != '管理员':

                info = {'id': item.id.id, 'avatar': item.avatar, 'name': item.name, 'signature': item.signature}
                allUsers.append(info)
        return Response({'data': allUsers})
