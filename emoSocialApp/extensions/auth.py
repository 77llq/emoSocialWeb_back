from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        
        token = super().get_token(user)
       
        token['name'] = user.username
        return token

    def validate(self, attrs):
        
        
        data = super().validate(attrs)
        
        refresh = self.get_token(self.user)
       
        data['token']=data['access']
       
        del data['access']
        
        data['expire'] = refresh.access_token.payload['exp']  
       
        data['username'] = self.user.username
        
        data['email'] = self.user.email
        return data