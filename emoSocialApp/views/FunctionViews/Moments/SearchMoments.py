

    # def list(self, request, *args, **kwargs):
    #     data = request.query_params.get('data')
    #     allMoments = Moments.objects.all()
    #     for item in allMoments:
    #         if data in item.postContent:
    #             print(item.postContent)
    #     return Response('123')

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.models import UserProfile, User, Moments, MomentsComment, MomentsLike


class SearchMomentsView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        momentsInfo = []
        data = request.query_params.get('data')
        moments = Moments.objects.all()
        for item in moments:
            if data in item.postContent:
                like_account = 0
                moment_form = {'momentId': item.id, 'postId': item.postId.id,
                               'postName': UserProfile.objects.get(id=item.postId).name,
                               'postAvatar': UserProfile.objects.get(id=item.postId).avatar, 'postTime': item.postTime,
                               'postContent': item.postContent, 'momentCommentInfo': [], 'momentLike': '',
                               'momentPic': item.postPic,
                               'momentVideo': item.postVideo, }
                for item2 in MomentsComment.objects.filter(momentId=item):
                    moment_comment_info = {
                        'commentName': '',
                        'commentContent': '',
                    }
                    commentName = UserProfile.objects.get(id=item2.commentId).name
                    commentContent = item2.commentContent
                    moment_comment_info['commentName'] = commentName
                    moment_comment_info['commentContent'] = commentContent
                    moment_form['momentCommentInfo'].append(moment_comment_info)
                for item3 in MomentsLike.objects.filter(momentId=item):
                    like_account = like_account + 1
                moment_form['momentLike'] = like_account
                momentsInfo.append(moment_form)
        return Response({"data": momentsInfo})

