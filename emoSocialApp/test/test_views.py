from django.test import TestCase, RequestFactory

from rest_framework.test import APIClient
from rest_framework import status
from emoSocialApp.models import User, UserProfile, Moments, MomentsLike, Board, Email
from emoSocialApp.views.AdminViews.CreateAdminAccount import CreateAdminAccountView
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers, AccountProfileSerializers
from emoSocialApp.views.CheckToken import CheckTokenView
from rest_framework_simplejwt.tokens import AccessToken

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