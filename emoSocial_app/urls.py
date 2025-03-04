from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from emoSocialApp.views.FunctionViews.Friends.CheckNewFriends import CheckNewFriendsView
from emoSocialApp.views.LoginViews.Register import AccountView
from emoSocialApp.views.LoginViews.CheckAccount import CheckAccountView
from emoSocialApp.views.LoginViews.RetrieveAccount import RetrieveAccountView
from emoSocialApp.views.LoginViews.Login import LoginView
from emoSocialApp.views.FunctionViews.Profile.EditProfile import EditProfileView
from emoSocialApp.views.FunctionViews.Profile.GetProfile import ProfileView
from emoSocialApp.views.FunctionViews.Friends.AddNewFriends import AddNewFriendsView
from emoSocialApp.views.FunctionViews.Friends.SendAddRequest import SendAddRequestView
from emoSocialApp.views.FunctionViews.Friends.AcceptNewFriends import AcceptNewFriendsView
from emoSocialApp.views.FunctionViews.Friends.RejectNewFriends import RejectNewFriendsView
from emoSocialApp.views.FunctionViews.Friends.GetFriendsInfo import GetFriendsInfoView
from emoSocialApp.views.FunctionViews.Friends.DeteletFriends import DeleteFriendsView
from emoSocialApp.views.FunctionViews.Friends.Follow import FollowView
from emoSocialApp.views.FunctionViews.Friends.Unfollow import UnfollowView
from emoSocialApp.views.FunctionViews.Friends.GetFollowInfo import GetFollowView
from emoSocialApp.views.FunctionViews.Friends.GetFollowingInfo import GetFollowingView
from emoSocialApp.views.FunctionViews.Profile.GetFans import GetFansInfoView
from emoSocialApp.views.FunctionViews.Profile.GetFansById import GetFansInfoByIdView
from emoSocialApp.views.FunctionViews.Emails.SendEmails import SendEmailView
from emoSocialApp.views.FunctionViews.Emails.CheckEmailBox import CheckEmailBoxView
from emoSocialApp.views.FunctionViews.Emails.CheckEmailContent import CheckEmailContentView
from emoSocialApp.views.FunctionViews.Emails.DeleteEmails import DeleteEmailsView
from emoSocialApp.views.FunctionViews.Moments.PostMoment import PostMomentView
from emoSocialApp.views.FunctionViews.Moments.GetSquareMoments import GetSquareMomentsView
from emoSocialApp.views.FunctionViews.Moments.CommentMoments import CommentMomentsView
from emoSocialApp.views.FunctionViews.Moments.LikeMoments import LikeMomentsView
from emoSocialApp.views.FunctionViews.Moments.GetFollowingMoments import GetFollowingMomentsView
from emoSocialApp.views.FunctionViews.Moments.GetPersonalMoments import GetPersonalMomentsView
from emoSocialApp.views.FunctionViews.Moments.GetFriendsMoments import GetFriendsMomentsView
from emoSocialApp.views.FunctionViews.Moments.GetFriendsPersonalMoments import GetFriendsPersonalMomentsView
from emoSocialApp.views.UploadFiles.UploadAvatar import UploadAvatarView
from emoSocialApp.views.UploadFiles.UploadProfileBp import UploadProfileBpView
from emoSocialApp.views.UploadFiles.UploadMomentsPic import UploadMomentsPicView
from emoSocialApp.views.UploadFiles.UploadVideos import UploadVideoView
from emoSocialApp.views.AdminViews.GetAllUsers import GetAllUsersView
from emoSocialApp.views.AdminViews.GetAllMoments import GetAllMomentsView
from emoSocialApp.views.FunctionViews.Friends.AddFriendsById import AddFriendsByIdView
from emoSocialApp.views.AdminViews.PostBoard import PostBoardView
from emoSocialApp.views.LoginViews.GetBoardContent import GetBoardContentView
from emoSocialApp.views.AdminViews.DeleteAccount import DeleteAccountView
from emoSocialApp.views.FunctionViews.Moments.DeleteMoments import DeleteMomentsView
from emoSocialApp.views.AdminViews.CreateAdminAccount import CreateAdminAccountView
from emoSocialApp.views.CheckToken import CheckTokenView
from emoSocialApp.views.FunctionViews.Moments.GetStrangerProfile import GetStrangerProfileView
from emoSocialApp.views.LoginViews.GetRecommendUsers import GetRecommendUsersView
from emoSocialApp.views.FunctionViews.Moments.SearchMoments import SearchMomentsView
from emoSocial_app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 验证token是否过期
    path("checkToken/", CheckTokenView.checkToken),
    # 登陆功能
    path('register/', AccountView.as_view({"get": "list", "post": "create"})),
    path('checkAccount/', CheckAccountView.as_view({"post": "create"})),
    path('retrieveAccount/', RetrieveAccountView.as_view({"post": "create", "put": "update", "get": "list"})),
    path('login/', LoginView.as_view({"post": "create", "get": "list"})),
    path('getBoardContent/', GetBoardContentView.as_view({"get": "list"})),
    # 编辑主页功能
    path('editProfile_apis/', EditProfileView.as_view({"post": "create", "put": "update"})),
    path('getProfile_apis/', ProfileView.as_view({"get": "list"})),
    # 好友功能
    path('addNewFriend_apis/', AddNewFriendsView.as_view({"get": "list"})),
    path('sendAddRequest_apis/', SendAddRequestView.as_view({"post": "create"})),
    path('checkNewFriends_apis/', CheckNewFriendsView.as_view({"get": "list"})),
    path('acceptNewFriends_apis/', AcceptNewFriendsView.as_view({"post": "create"})),
    path('rejectNewFriends_apis/', RejectNewFriendsView.as_view({"delete": "destroy"})),
    path('getFriendsInfo_apis/', GetFriendsInfoView.as_view({"get": "list"})),
    path('deteletFriends_apis/', DeleteFriendsView.as_view({"delete": "destroy"})),
    path('follow_apis/', FollowView.as_view({"post": "create"})),
    path('unfollow_apis/', UnfollowView.as_view({"delete": "destroy"})),
    path('getFollowInfo_apis/', GetFollowView.as_view({"get": "list"})),
    path('getFollowingInfo_apis/', GetFollowingView.as_view({"get": "list"})),
    path('getFansInfo_apis/', GetFansInfoView.as_view({"get": "list"})),
    path('getFansInfoById_apis/', GetFansInfoByIdView.as_view({"get": "list"})),
    path('addFriendsById_apis/', AddFriendsByIdView.as_view({"post": "create"})),
    # 邮件功能
    path('sendEmails_apis/', SendEmailView.as_view({"post": "create"})),
    path('checkEmailBox_apis/', CheckEmailBoxView.as_view({"get": "list"})),
    path('checkEmailContent_apis/', CheckEmailContentView.as_view({"get": "list"})),
    path('deleteEmails_apis/', DeleteEmailsView.as_view({"delete": "destroy"})),
    # 朋友圈功能
    path('postMoment_apis/', PostMomentView.as_view({"post": "create"})),
    path('getSquareMoments_apis/', GetSquareMomentsView.as_view({"get": "list"})),
    path('commentMoments_apis/', CommentMomentsView.as_view({"post": "create"})),
    path('likeMoments_apis/', LikeMomentsView.as_view({"post": "create"})),
    path('getFollowingMoments_apis/', GetFollowingMomentsView.as_view({"get": "list"})),
    path('getPersonalMoments_apis/', GetPersonalMomentsView.as_view({"get": "list"})),
    path('getFriendsMoments_apis/', GetFriendsMomentsView.as_view({"get": "list"})),
    path('deleteMoments_apis/', DeleteMomentsView.as_view({"delete": "destroy"})),
    path('getFriendsPersonalMoments_apis/', GetFriendsPersonalMomentsView.as_view({"get": "list"})),
    path('getStrangerProfile_apis/', GetStrangerProfileView.as_view({"get": "list"})),
    # #
    path("uploadAvatar_apis/", UploadAvatarView.saveImage),
    re_path(r'^media/user(?P<path>.*)$', serve, {'document_root': settings.USER_AVATAR_ROOT}),
    path("uploadProfileBp_apis/", UploadProfileBpView.saveImage),
    re_path(r'^media/profileBp(?P<path>.*)$', serve, {'document_root': settings.USER_PROFILEBP_ROOT}),
    path("uploadMomentsPic_apis/", UploadMomentsPicView.saveImage),
    re_path(r'^moments(?P<path>.*)$', serve, {'document_root': settings.USER_MOMENTS_PIC_ROOT}),
    path("uploadMomentsVideo_apis/", UploadVideoView.saveImage),
    re_path(r'^videos(?P<path>.*)$', serve, {'document_root': settings.USER_MOMENTS_VIDEO_ROOT}),
    # 管理员
    path('getAllUsers_apis/', GetAllUsersView.as_view({"get": "list"})),
    path('getAllMoments_apis/', GetAllMomentsView.as_view({"get": "list"})),
    path('postBoard_apis/', PostBoardView.as_view({"post": "create"})),
    path('deleteAccount_apis/', DeleteAccountView.as_view({"delete": "destroy"})),
    path('createAdminAccount_apis/', CreateAdminAccountView.as_view({"post": "create"})),

    path('getRecommendUsers_apis/', GetRecommendUsersView.as_view({"get": "list"})),
    path('searchMoments_apis/', SearchMomentsView.as_view({"get": "list"})),
]
