from django.test import TestCase, RequestFactory

from rest_framework.test import APIClient
from rest_framework import status
from emoSocialApp.models import User, UserProfile, Moments, MomentsComment, MomentsLike, Board, Email, FriendsRequest, Friends, Fans
from emoSocialApp.views.AdminViews.CreateAdminAccount import CreateAdminAccountView
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers, AccountProfileSerializers
from emoSocialApp.views.CheckToken import CheckTokenView
from rest_framework_simplejwt.tokens import AccessToken
from emoSocialApp.views.FunctionViews.Emails.SendEmails import SendEmailView as SendEmailView


###### Moments tests
class commentMomentsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='user2',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.moment = Moments.objects.create(postId=self.user1, postContent='Test Moment')
        self.token = str(AccessToken.for_user(self.user1))

    def test_comment_moments(self):
        data = {
            'Token': self.token,
            'commentMomentId': self.moment.id,
            'commentContent': 'This is a comment'
        }

        response = self.client.post('/commentMoments_apis/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'success'})

        self.assertTrue(MomentsComment.objects.filter(momentId=self.moment, commentId=self.user1, commentContent='This is a comment').exists())

class deleteMomentsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(
                id='123',
                account='user1',
                password='password123',
                type='普通用户',
                idNumber='123456789012345678'
            )

        self.moment = Moments.objects.create(postId=self.user1, postContent='Test Moment')
    def test_delete_moment(self):
        query_params = {
            'id': self.moment.id
        }
        response = self.client.delete('/deleteMoments_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'success'})

class getFollowingMonmentTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='user2',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.user1 = UserProfile.objects.create(
            id=self.user1,
            name='user1',
            avatar='avatar_url1',
            signature='Test1 Signature',
            birthday='2000-01-01'
        )
        self.user2 = UserProfile.objects.create(
            id=self.user2,
            name='user2',
            avatar='avatar_url2',
            signature='Test2 Signature',
            birthday='2000-01-01'
        )

        Fans.objects.create(userId=self.user2.id, fansId=self.user1.id)
        self.moment = Moments.objects.create(postId=self.user2.id, postContent='Test Moment', postPic='pic.jpg', postVideo='video.mp4')
        MomentsComment.objects.create(momentId=self.moment, commentId=self.user1.id, commentContent='Nice post!')
        MomentsLike.objects.create(momentId=self.moment, likeId=self.user1.id)

        self.token = str(AccessToken.for_user(self.user1))

    def test_get_following_moments_success(self):
        query_params = {
            'token': self.token
        }

        response = self.client.get('/getFollowingMoments_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        expected_data = [
            {
                'momentId': self.moment.id,
                'postId': str(self.user2.id),
                'postName': 'user2',
                'postAvatar': 'avatar_url2',
                'postTime': self.moment.postTime,  
                'postContent': 'Test Moment',
                'momentCommentInfo': [
                    {
                        'commentName': 'user1',
                        'commentContent': 'Nice post!'
                    }
                ],
                'momentLike': 1,
                'momentPic': 'pic.jpg',
                'momentVideo': 'video.mp4'
            }
        ]
        self.assertEqual(response.data['data'], expected_data)

class getFriendsMonmentTest(TestCase) :
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user1 = UserProfile.objects.create(
            id=self.user1,
            name='user1',
            avatar='avatar_url1',
            signature='Test1 Signature',
            birthday='2000-01-01'
        )

        self.moment = Moments.objects.create(postId=self.user1.id, postContent='Test Moment', postPic='pic.jpg', postVideo='video.mp4')
        MomentsComment.objects.create(momentId=self.moment, commentId=self.user1.id, commentContent='Nice post!')
        MomentsLike.objects.create(momentId=self.moment, likeId=self.user1.id)

    def test_get_friends_moments_success(self):
        query_params = {
            'id': self.user1.id
        }

        response = self.client.get('/getFriendsMoments_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        expected_data = [
                {
                    'momentId': self.moment.id,
                    'postId': str(self.user1.id),  
                    'postName': 'user1',
                    'postAvatar': 'avatar_url1',
                    'postTime': self.moment.postTime,
                    'postContent': 'Test Moment',
                    'momentCommentInfo': [
                        {
                            'commentName': 'user1',
                            'commentContent': 'Nice post!'
                        }
                    ],
                    'momentLike': 1,
                    'momentPic': 'pic.jpg',
                    'momentVideo': 'video.mp4'
                }
            ]
        self.assertEqual(response.data['data'], expected_data)

class getFriendsPersonalMomentsTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='user2',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.user1 = UserProfile.objects.create(
            id=self.user1,
            name='user1',
            avatar='avatar_url1',
            signature='Test1 Signature',
            birthday='2000-01-01'
        )
        self.user2 = UserProfile.objects.create(
            id=self.user2,
            name='user2',
            avatar='avatar_url2',
            signature='Test2 Signature',
            birthday='2000-01-01'
        )

        self.moment = Moments.objects.create(postId=self.user2.id, postContent='Test Moment', postPic='pic.jpg', postVideo='video.mp4')
        MomentsComment.objects.create(momentId=self.moment, commentId=self.user1.id, commentContent='Nice post!')
        MomentsLike.objects.create(momentId=self.moment, likeId=self.user1.id)

    def test_get_friends_personal_moments_success(self):
        query_params = {
            'friendId': self.user2.id
        }

        response = self.client.get('/getFriendsPersonalMoments_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1) 

        expected_data = [
            {
                'momentId': self.moment.id,
                'postId': str(self.user2.id), 
                'postName': 'user2',
                'postAvatar': 'avatar_url2',
                'postTime': self.moment.postTime,
                'postContent': 'Test Moment',
                'momentCommentInfo': [
                    {
                        'commentName': 'user1',
                        'commentContent': 'Nice post!'
                    }
                ],
                'momentLike': 1,
                'momentPic': 'pic.jpg',
                'momentVideo': 'video.mp4'
            }
        ]
        self.assertEqual(response.data['data'], expected_data)

class getPersonalMomentsTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user1 = UserProfile.objects.create(
            id=self.user1,
            name='user1',
            avatar='avatar_url1',
            signature='Test1 Signature',
            birthday='2000-01-01'
        )

        self.moment = Moments.objects.create(postId=self.user1.id, postContent='Test Moment', postPic='pic.jpg', postVideo='video.mp4')
        MomentsComment.objects.create(momentId=self.moment, commentId=self.user1.id, commentContent='Nice post!')
        MomentsLike.objects.create(momentId=self.moment, likeId=self.user1.id)
        self.token = str(AccessToken.for_user(self.user1))
    def test_get_personal_moments_success(self):
        query_params = {
            'token': self.token
        }

        response = self.client.get('/getPersonalMoments_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

        expected_data = [
            {
                'momentId': self.moment.id,
                'postId': str(self.user1.id),  # 将 postId 转换为字符串
                'postName': 'user1',
                'postAvatar': 'avatar_url1',
                'postTime': self.moment.postTime,
                'postContent': 'Test Moment',
                'momentCommentInfo': [
                    {
                        'commentName': 'user1',
                        'commentContent': 'Nice post!'
                    }
                ],
                'momentLike': 1,
                'momentPic': 'pic.jpg',
                'momentVideo': 'video.mp4'
            }
        ]
        self.assertEqual(response.data['data'], expected_data)

class getPersonalMomentTest(TestCase) :
    def setUp(self):
        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='user2',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.user1 = UserProfile.objects.create(
            id=self.user1,
            name='user1',
            avatar='avatar_url1',
            signature='Test1 Signature',
            birthday='2000-01-01'
        )
        self.user2 = UserProfile.objects.create(
            id=self.user2,
            name='user2',
            avatar='avatar_url2',
            signature='Test2 Signature',
            birthday='2000-01-01'
        )

        self.moment1 = Moments.objects.create(postId=self.user1.id, postContent='Test Moment 1', postPic='pic1.jpg', postVideo='video1.mp4')
        self.moment2 = Moments.objects.create(postId=self.user2.id, postContent='Test Moment 2', postPic='pic2.jpg', postVideo='video2.mp4')

        MomentsComment.objects.create(momentId=self.moment2, commentId=self.user1.id, commentContent='Nice post!')
        MomentsLike.objects.create(momentId=self.moment2, likeId=self.user1.id)
    def test_get_square_moments(self):

        response = self.client.get('/getSquareMoments_apis/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 2)

class getStrangeProfileTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='user2',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.user1 = UserProfile.objects.create(
            id=self.user1,
            name='user1',
            avatar='avatar_url1',
            signature='Test1 Signature',
            birthday='2000-01-01',
            profileBp='background.jpg',
            email='user1@test.com',
            gender='female'
        )

        self.moment = Moments.objects.create(postId=self.user1.id, postContent='Test Moment', postPic='pic.jpg', postVideo='video.mp4')
        Fans.objects.create(userId=self.user1.id, fansId=self.user2)

    def test_get_stranger_profile_success(self):
        query_params = {
            'id': self.user1.id
        }

        response = self.client.get('/getStrangerProfile_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class likeMomentTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.moment = Moments.objects.create(postId=self.user1, postContent='Test Moment', postPic='pic.jpg', postVideo='video.mp4')
        self.token = str(AccessToken.for_user(self.user1))
    def test_like_moments_success(self):
        data = {
            'token': self.token,
            'momentId': self.moment.id
        }

        response = self.client.post('/likeMoments_apis/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'success'})
        self.assertTrue(MomentsLike.objects.filter(momentId=self.moment, likeId=self.user1).exists())

class postMomentTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )


        self.token = str(AccessToken.for_user(self.user1))

        self.sensitive_words = ['badword1', 'badword2']
        with open('static/sensitive_words/words.txt', 'w', encoding='utf-8') as f:
            for word in self.sensitive_words:
                f.write(word + '\n')
    
    def test_post_moment_success(self):
        data = {
            'data': {
                '_value': {
                    'token': self.token,
                    'post_content': 'This is a test moment',
                    'post_pic': 'pic.jpg',
                    'post_video': 'video.mp4'
                }
            }
        }
        response = self.client.post('/postMoment_apis/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'success'})

        self.assertTrue(Moments.objects.filter(postId=self.user1, postContent='This is a test moment').exists())

    def test_post_moment_sensitive_content(self):
        data = {
            'data': {
                '_value': {
                    'token': self.token,
                    'post_content': 'This is a badword1 moment',
                    'post_pic': 'pic.jpg',
                    'post_video': 'video.mp4'
                }
            }
        }

        response = self.client.post('/postMoment_apis/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'sensitive'})
        self.assertFalse(Moments.objects.filter(postId=self.user1, postContent='This is a badword1 moment').exists())

class seearchMomentTest(TestCase) :
     def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='user1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )
        self.user1 = UserProfile.objects.create(
            id=self.user1,
            name='user1',
            avatar='avatar_url1',
            signature='Test1 Signature',
            birthday='2000-01-01',
            profileBp='background.jpg',
            email='user1@test.com',
            gender='female'
        )

        self.moment1 = Moments.objects.create(postId=self.user1.id, postContent='This is a test moment', postPic='pic1.jpg', postVideo='video1.mp4')
        self.moment2 = Moments.objects.create(postId=self.user1.id, postContent='Another moment', postPic='pic2.jpg', postVideo='video2.mp4')


        MomentsComment.objects.create(momentId=self.moment1, commentId=self.user1.id, commentContent='Nice post!')
        MomentsLike.objects.create(momentId=self.moment1, likeId=self.user1.id)

     def test_search_moments_success(self):
        query_params = {
            'data': 'test'
        }
        response = self.client.get('/searchMoments_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
