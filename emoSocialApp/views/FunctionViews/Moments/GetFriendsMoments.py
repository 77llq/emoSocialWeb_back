from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from emoSocialApp.models import UserProfile, User, Moments, MomentsComment, MomentsLike


class GetFriendsMomentsView(ModelViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        momentsInfo = []
        user_id = request.query_params.get('id')
        user_id = User.objects.get(id=user_id)
        friend_moments = Moments.objects.filter(postId=user_id).order_by('-postTime')
        for item in friend_moments:
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
