from django.http import JsonResponse
from rest_framework.response import Response

from emoSocialApp.extensions.auth import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import os

from emoSocial_app.settings import USER_AVATAR_ROOT


class UploadAvatarView:
    def saveImage(request):
        response = {}
        # 获取前端发来的的file对象
        file = request.FILES.get('file')
        try:
            file_path = os.path.join(USER_AVATAR_ROOT, file.name)
            # 保存图片
            with open(file_path, 'wb+') as f:
                f.write(file.read())
                f.close()
            response['file'] = file.name  # 返回新的文件名
            response['code'] = 0
            response['msg'] = "图片上传成功！"
        except:
            response['file'] = ''
            response['code'] = 1
            response['msg'] = "图片上传失败！"
        return JsonResponse(response)
