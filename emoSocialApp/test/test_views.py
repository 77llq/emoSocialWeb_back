from django.test import TestCase, RequestFactory

from rest_framework.test import APIClient
from rest_framework import status
from emoSocialApp.models import User, UserProfile, Moments, MomentsLike, Board, Email, FriendsRequest, Friends, Fans
from emoSocialApp.views.AdminViews.CreateAdminAccount import CreateAdminAccountView
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers, AccountProfileSerializers
from emoSocialApp.views.CheckToken import CheckTokenView
from rest_framework_simplejwt.tokens import AccessToken
from emoSocialApp.views.FunctionViews.Emails.SendEmails import SendEmailView as SendEmailView


#######AdminViews
class accountViewTest(TestCase):
    def setUp(self):

        self.client = APIClient()
        self.factory = RequestFactory()
        self.user = User.objects.create(
            id='1233',
            account='putong'
        )
    def test_create_admin_account_already_exist(self):
        
        data = {
            'dataForm': {
                'id': '1233',
                'account': 'putong'
            }
        }
        response = self.client.post('/createAdminAccount_apis/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response)
        self.assertEqual(response.data['code'], 'already')

    def test_create_admin_account_error(self):
        data = {
            "dataForm": {
            "id": "4564567",
            "account": "adminne",
            "password": "password",
            "type": "管理员",
            "idNumber": "1312412412"
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post('/createAdminAccount_apis/', data=data, format='json',headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(response.data['code'], 'error')

class deleteAccountTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        user1 = User.objects.create(id='123', account='usertest1')
    def test_delete_account(self):
        response = self.client.delete('/deleteAccount_apis/?id=123')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'success')

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id='123')

class allMomentTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            id='123',
            account='usertest1',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user_profile = UserProfile.objects.create(
            id=self.user,
            avatar='avatar_url',
            name='Test User',
            birthday='2000-01-01'
        )

        self.moment = Moments.objects.create(
            postId=self.user,
            postContent='Test content',
            postTime='2025-01-01',
            postVideo='video_url',
            postPic='pic_url'
        )
        self.moment_like = MomentsLike.objects.create(
            momentId=self.moment,
            likeId=self.user
        )
    def test_get_all_moments_success(self):
    
        response = self.client.get('/getAllMoments_apis/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

        moment_data = response.data['data'][0]
        self.assertEqual(moment_data['id'], '123')
        self.assertEqual(moment_data['account'], 'usertest1')
        self.assertEqual(moment_data['avatar'], 'avatar_url')
        self.assertEqual(moment_data['name'], 'Test User')
        self.assertEqual(moment_data['content'], 'Test content')
        self.assertEqual(moment_data['postTime'], '2025-01-01')
        self.assertEqual(moment_data['video'], 'video_url')
        self.assertEqual(moment_data['pic'], 'pic_url')
        self.assertEqual(moment_data['likes'], 1)
        self.assertEqual(moment_data['momentId'], self.moment.id)

class getAllUsersTest(TestCase) :
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user_profile = UserProfile.objects.create(
            id=self.user,
            avatar='avatar_url',
            name='Test User',
            email='test@example.com',
            gender='Male',
            birthday='2000-01-01'
        )
    def test_get_all_users_success(self):
        response = self.client.get('/getAllUsers_apis/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

        user_data = response.data['data'][0]
        self.assertEqual(user_data['id'], '123')
        self.assertEqual(user_data['account'], 'usertest')
        self.assertEqual(user_data['avatar'], 'avatar_url')
        self.assertEqual(user_data['name'], 'Test User')
        self.assertEqual(user_data['email'], 'test@example.com')
        self.assertEqual(user_data['gender'], 'Male')
        self.assertEqual(str(user_data['birthday']), '2000-01-01')
        self.assertEqual(user_data['idNumber'], '123456789012345678')

class boardTest(TestCase) :
    def setUp(self):
        # 创建测试客户端
        self.client = APIClient()

        self.user = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user_profile = UserProfile.objects.create(
            id=self.user,
            name='Test User',
            birthday='2000-01-01'
        )

        self.token = str(AccessToken.for_user(self.user))

    def test_post_board(self):
        data = {
                'token': self.token,
                'board': {
                    'board_topic': 'Test Topic',
                    'board_content': 'Test Content'
                }
            }

        response = self.client.post('/postBoard_apis/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'success')

        board = Board.objects.get(postId=self.user)
        self.assertEqual(board.postTopic, 'Test Topic')
        self.assertEqual(board.postContent, 'Test Content')



class checkTokenTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    def test_check_token_success(self):
        request = self.factory.get('/checkToken/', {'token': '123'})

        response = CheckTokenView.checkToken(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), '123')

#########Emails
class checkEmailTest(TestCase) :
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='usertest2',
            password='password123',
            type='普通用户',
            idNumber='123456789012345679'
        )


        self.user_profile = UserProfile.objects.create(
            id=self.user,
            name='Test User',
            birthday='2000-01-01'
        )

        self.user_profile = UserProfile.objects.create(
            id=self.user2,
            name='Test User2',
            birthday='2000-01-01'
        )

        self.token = str(AccessToken.for_user(self.user2))

        self.email = Email.objects.create(
            receiveId=self.user2,
            emailTopic='Test Topic',
            emailContent='Test Content',
            sendTime='2025-01-01 12:00:00',
            sendId=self.user
        )
    def test_check_email_box_success(self):
        response = self.client.get('/checkEmailBox_apis/', {'token': self.token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['email_info']), 1)

        email_data = response.data['email_info'][0]
        self.assertEqual(email_data['send_name'], 'Test User')
        self.assertEqual(email_data['send_time'], '2025-01-01 12:00:00')
        self.assertEqual(email_data['email_id'], self.email.id)
        self.assertEqual(email_data['email_topic'], 'Test Topic')
        self.assertEqual(email_data['email_content'], 'Test Content')

class checkEmailContent(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.sender = User.objects.create(
            id='123',
            account='sender',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.receiver = User.objects.create(
            id='456',
            account='receiver',
            password='password456',
            type='普通用户',
            idNumber='987654321098765432'
        )

        self.sender_profile = UserProfile.objects.create(
            id=self.sender,
            name='Sender User',
            email='sender@test.com',
            birthday='2000-01-01'
        )

        self.receiver_profile = UserProfile.objects.create(
            id=self.receiver,
            name='Receiver User',
            email='receiver@test.com',
            birthday='2000-01-01'
        )

        self.email = Email.objects.create(
            id='789',
            emailTopic='Test Topic',
            emailContent='Test Content',
            sendTime='2025-01-01 12:00:00',
            sendId=self.sender,
            receiveId=self.receiver
        )
    def test_check_email_content_success(self):
        response = self.client.get('/checkEmailContent_apis/', {'email_id': '789'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        email_info = response.data['email_info']
        self.assertEqual(email_info['email_topic'], 'Test Topic')
        self.assertEqual(email_info['send_name'], 'Sender User')
        self.assertEqual(email_info['send_email'], 'sender@test.com')
        self.assertEqual(email_info['send_time'], '2025-01-01 12:00:00')
        self.assertEqual(email_info['receive_name'], 'Receiver User')
        self.assertEqual(email_info['email_content'], 'Test Content')
        self.assertEqual(email_info['receive_email'], 'receiver@test.com')

class deleteEmailTest(TestCase) :
    def setUp(self):
        self.client = APIClient()

        self.sender = User.objects.create(
            id='123',
            account='sender',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.receiver = User.objects.create(
            id='456',
            account='receiver',
            password='password456',
            type='普通用户',
            idNumber='987654321098765432'
        )

        self.email = Email.objects.create(
            id='123',
            emailTopic='Test Topic',
            emailContent='Test Content',
            sendTime='2025-01-01 12:00:00',
            sendId=self.sender,
            receiveId=self.receiver
        )

    def test_delete_email_success(self):
        response = self.client.delete('/deleteEmails_apis/', {'email_id': '123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class sendEmailTest(TestCase) :

    def setUp(self):
        self.client = APIClient()

        self.sender = User.objects.create(
            id='123',
            account='sender',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )
        self.receiver = User.objects.create(
            id='456',
            account='receiver',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.sender_profile = UserProfile.objects.create(
            id=self.sender,
            name='Sender User',
            email='sender@test.com',
            birthday='2000-01-01'
        )

        self.receiver_profile = UserProfile.objects.create(
            id=self.receiver,
            name='Receiver User',
            email='receiver@test.com',
            birthday='2000-01-01'
        )

        self.token = str(AccessToken.for_user(self.sender))
def test_sen_email(self):
    SendEmailView.time_trans()
    data = {
            'email_info': {
                '_value': {
                    'token': self.token,
                    'receive_id': '789',
                    'receive_email': 'receiver@example.com',
                    'email_topic': 'Test Topic',
                    'email_content': 'Test Content'
                }
            }
        }

    response = self.client.post('/sendEmails_apis/', data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['code'], 'success')

    email = Email.objects.get(receiveId=self.receiver)
    self.assertEqual(email.emailTopic, 'Test Topic')
    self.assertEqual(email.emailContent, 'Test Content')
    self.assertEqual(email.sendId, self.sender)
    self.assertEqual(email.receiveId, self.receiver)

#######Friends

class accepetfriend(TestCase) :
    def setUp(self):
        self.client = APIClient()

        self.sender = User.objects.create(
            id='123',
            account='sender',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.receiver = User.objects.create(
            id='456',
            account='receiver',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.sender_profile = UserProfile.objects.create(
            id=self.sender,
            name='Sender User',
            email='sender@test.com',
            birthday='2000-01-01'
        )

        self.receiver_profile = UserProfile.objects.create(
            id=self.receiver,
            name='Receiver User',
            email='receiver@test.com',
            birthday='2000-01-01'
        )

        self.token = str(AccessToken.for_user(self.sender))

    def test_send_email(self):
        data = {
            'email_info': {
                '_value': {
                    'token': self.token,
                    'receive_id': '456',
                    'receive_email': 'receiver@test.com',
                    'email_topic': 'Test Topic',
                    'email_content': 'Test Content'
                }
            }
        }

        response = self.client.post('/sendEmails_apis/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'success')

        email = Email.objects.get(receiveId=self.receiver)
        self.assertEqual(email.emailTopic, 'Test Topic')
        self.assertEqual(email.emailContent, 'Test Content')
        self.assertEqual(email.sendId, self.sender)
        self.assertEqual(email.receiveId, self.receiver)

class addFriendById(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.target_friend = User.objects.create(
            id='456',
            account='friendtest',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.token = str(AccessToken.for_user(self.user))
    def test_add_friend_success(self):
        data = {
            'token': self.token,
            'postId': '456'
        }

        response = self.client.post('/addFriendsById_apis/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'success')
        friend_request = FriendsRequest.objects.get(receiveRequestId=self.target_friend, sendRequestId=self.user)
        self.assertIsNotNone(friend_request)

    def test_add_friend_self(self):
        data = {
            'token': self.token,
            'postId': '123'
        }
        response = self.client.post('/addFriendsById_apis/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'self')
        self.assertFalse(FriendsRequest.objects.filter(receiveRequestId=self.user, sendRequestId=self.user).exists())
    
    def test_add_friend_repeat(self):
        FriendsRequest.objects.create(receiveRequestId=self.target_friend, sendRequestId=self.user)
        data = {
            'token': self.token,
            'postId': '456'
        }

        response = self.client.post('/addFriendsById_apis/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'repeat')

    def test_add_friend_already(self):
        Friends.objects.create(userId=self.user, friendId=self.target_friend)
        data = {
            'token': self.token,
            'postId': '456'
        }

        response = self.client.post('/addFriendsById_apis/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'already')

class addNewFriendsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.target_friend = User.objects.create(
            id='456',
            account='friendtest',
            password='password456',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.target_friend_profile = UserProfile.objects.create(
            id=self.target_friend,
            signature='Test Signature',
            avatar='avatar_url',
            name='Friend User',
            birthday='2000-01-01'
        )

        self.token = str(AccessToken.for_user(self.user))

    def test_add_new_friend_success(self):
        params = {
            'token': self.token,
            'target_account': 'friendtest'
        }

        response = self.client.get('/addNewFriend_apis/', params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'success')
        
        target_info = response.data['target_info']
        self.assertEqual(target_info['friend_signature'], 'Test Signature')
        self.assertEqual(target_info['friend_avatar'], 'avatar_url')
        self.assertEqual(target_info['friend_name'], 'Friend User')

    def test_add_new_friend_error(self):
        params = {
            'token': self.token,
            'target_account': 'friendtest2'
        }

        response = self.client.get('/addNewFriend_apis/', params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'error')

class checkNewFriends(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.sender = User.objects.create(
            id='456',
            account='friendtest',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.sender_profile = UserProfile.objects.create(
            id=self.sender,
            name='Sender User',
            avatar='avatar_url',
            signature='Test Signature',
            birthday='2000-01-01'
        )

        self.friend_request = FriendsRequest.objects.create(
            sendRequestId=self.sender,
            receiveRequestId=self.user
        )

        self.token = str(AccessToken.for_user(self.user))
    def test_check_new_friends_success(self):
        params = {
            'token': self.token
        }
        response = self.client.get('/checkNewFriends_apis/', params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        request_info = response.data['request_info']
        self.assertEqual(len(request_info), 1)
        self.assertEqual(request_info[0]['avatar'], 'avatar_url')
        self.assertEqual(request_info[0]['name'], 'Sender User')
        self.assertEqual(request_info[0]['signature'], 'Test Signature')
        self.assertEqual(request_info[0]['id'], '456')

"""
class deleteFriendsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='friendtest',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.user2 = UserProfile.objects.create(
            id=self.user2,
            signature='Test Signature',
            avatar='avatar_url',
            name='Friend User',
            birthday='2000-01-01'
        )

        self.token = str(AccessToken.for_user(self.user1))
    def test_delete_friends_success(self):

        params = {
            'token': self.token,
            'target_account': 'friendtest'
        }

        self.client.get('/addNewFriend_apis/', params)

        response = self.client.delete('/deteletFriends_apis/', {
            'delete_id': self.user2.id,
            'token': self.token
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'success'})
"""

class followTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )
        self.user2 = User.objects.create(
            id='456',
            account='friendtest',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )
        self.token = str(AccessToken.for_user(self.user))
    
    def test_follow_user(self): 
        data = {
            'token': self.token,
            'follow_id': self.user2.id
        }

        response = self.client.post('/follow_apis/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'success'})
        self.assertTrue(Fans.objects.filter(userId=self.user2, fansId=self.user).exists())

    def test_follow_user_already_followed(self):
        Fans.objects.create(userId=self.user2, fansId=self.user)

        data = {
            'token': self.token,
            'follow_id': self.user2.id
        }

        response = self.client.post('/follow_apis/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'already'})

class getFollowTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='friendtest',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.user3 = User.objects.create(
            id='789',
            account='friendtest2',
            password='password4567',
            type='普通用户',
            idNumber='123456789012345670'
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
        self.user3 = UserProfile.objects.create(
            id=self.user3,
            name='user3',
            avatar='avatar_url3',
            signature='Test3 Signature',
            birthday='2000-01-01'
        )

        Fans.objects.create(userId=self.user2.id, fansId=self.user1.id)
        Fans.objects.create(userId=self.user3.id, fansId=self.user1.id)

        self.token = str(AccessToken.for_user(self.user1))
    def test_get_follow_list_success(self):
        query_params = {
            'token': self.token
        }

        response = self.client.get('/getFollowInfo_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['user_info']), 2) 

        expected_data = [
            {
                'user_id': str(self.user2.id),
                'name': 'user2',
                'avatar': 'avatar_url2'
            },
            {
                'user_id': str(self.user3.id),
                'name': 'user3',
                'avatar': 'avatar_url3'
            }
        ]
        self.assertEqual(response.data['user_info'], expected_data)

class getFolloingInfoTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='friendtest',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.user3 = User.objects.create(
            id='789',
            account='friendtest2',
            password='password4567',
            type='普通用户',
            idNumber='123456789012345670'
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
        self.user3 = UserProfile.objects.create(
            id=self.user3,
            name='user3',
            avatar='avatar_url3',
            signature='Test3 Signature',
            birthday='2000-01-01'
        )

        Fans.objects.create(userId=self.user1.id, fansId=self.user2.id)
        Fans.objects.create(userId=self.user1.id, fansId=self.user3.id)

        self.token = str(AccessToken.for_user(self.user1))
    def test_get_following_list_success(self):
        query_params = {
            'token': self.token
        }

        response = self.client.get('/getFollowingInfo_apis/', query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['fans_info']), 2)  

        expected_data = [
            {
                'fans_id': str(self.user2.id), 
                'name': 'user2',
                'avatar': 'avatar_url2'
            },
            {
                'fans_id': str(self.user3.id),  
                'name': 'user3',
                'avatar': 'avatar_url3'
            }
        ]
        self.assertEqual(response.data['fans_info'], expected_data)

class getFriendInfoTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='friendtest',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        self.user3 = User.objects.create(
            id='789',
            account='friendtest2',
            password='password4567',
            type='普通用户',
            idNumber='123456789012345670'
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
        self.user3 = UserProfile.objects.create(
            id=self.user3,
            name='user3',
            avatar='avatar_url3',
            signature='Test3 Signature',
            birthday='2000-01-01'
        )

        Friends.objects.create(userId=self.user1.id, friendId=self.user2.id, intimacy='5')
        FriendsRequest.objects.create(sendRequestId=self.user3.id, receiveRequestId=self.user1.id)
        self.token = str(AccessToken.for_user(self.user1))

    def test_get_friends_info_success(self):
        query_params = {
            'token': self.token
        }

        response = self.client.get('/getFriendsInfo_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['friends_info']), 1) 

        expected_data = [
            {
                'friend_id': str(self.user2.id), 
                'friend_name': 'user2',
                'friend_avatar': 'avatar_url2',
                'friend_signature': 'Test2 Signature',
                'intimacy': '5'
            }
        ]
        self.assertEqual(response.data['friends_info'], expected_data)
        self.assertEqual(response.data['newFriends_request'], 1)

"""
class rejectTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create(
            id='123',
            account='usertest',
            password='password123',
            type='普通用户',
            idNumber='123456789012345678'
        )

        self.user2 = User.objects.create(
            id='456',
            account='friendtest',
            password='password456',
            type='普通用户',
            idNumber='123456789012345679'
        )

        FriendsRequest.objects.create(sendRequestId=self.user2, receiveRequestId=self.user1)
        self.token = str(AccessToken.for_user(self.user1))
    def test_reject_new_friends_success(self):
        query_params = {
            'token': self.token,
            'apply_id': self.user2.id
        }

        response = self.client.delete('/rejectNewFriends_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'deleted')

        self.assertFalse(FriendsRequest.objects.filter(sendRequestId=self.user2, receiveRequestId=self.user1).exists())
"""

class requestTest(TestCase):
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

        self.token = str(AccessToken.for_user(self.user1))
    def test_send_add_request_success(self):
        data = {
            'token': self.token,
            'account': 'user2'
        }

        response = self.client.post('/sendAddRequest_apis/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'success'})
        self.assertTrue(FriendsRequest.objects.filter(sendRequestId=self.user1, receiveRequestId=self.user2).exists())

    def test_send_add_request_repeat(self):
        FriendsRequest.objects.create(sendRequestId=self.user1, receiveRequestId=self.user2)

        data = {
            'token': self.token,
            'account': 'user2'
        }

        response = self.client.post('/sendAddRequest_apis/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'repeat'})

    def test_send_add_request_already_friends(self):
        Friends.objects.create(userId=self.user1, friendId=self.user2)
        Friends.objects.create(userId=self.user2, friendId=self.user1)

        data = {
            'token': self.token,
            'account': 'user2'
        }

        response = self.client.post('/sendAddRequest_apis/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'already'})
    def test_send_add_request_self(self):
        data = {
            'token': self.token,
            'account': 'user1'
        }

        response = self.client.post('/sendAddRequest_apis/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'self'})

"""
class unfollowTest(TestCase):
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
        Fans.objects.create(userId=self.user2, fansId=self.user1)
        self.token = str(AccessToken.for_user(self.user1))

    def test_unfollow_success(self):
        query_params = {
            'token': self.token,
            'unfollow_id': self.user2.id
        }

        response = self.client.delete('/unfollow_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'code': 'success'})
        self.assertFalse(Fans.objects.filter(userId=self.user2, fansId=self.user1).exists())
"""

class getFansTest(TestCase) :
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
        Fans.objects.create(userId=self.user2, fansId=self.user1)
        Fans.objects.create(userId=self.user1, fansId=self.user2)
        self.token = str(AccessToken.for_user(self.user1))
    def test_get_fans_info_success(self):
        query_params = {
            'token': self.token
        }
        response = self.client.get('/getFansInfo_apis/', query_params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'follow_num': 1, 'fans_num': 1})