from django.test import TestCase, RequestFactory

from rest_framework.test import APIClient
from rest_framework import status
from emoSocialApp.models import User
from emoSocialApp.views.AdminViews.CreateAdminAccount import CreateAdminAccountView
from emoSocialApp.Serializers.RegisterSerializers import AccountSerializers, AccountProfileSerializers
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
        user1 = User.objects.create(id='123', account='usertest1')
    def test_delete_account(self):
        response = self.client.delete('/deleteAccount_apis/?id=123')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'success')

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id='123')
