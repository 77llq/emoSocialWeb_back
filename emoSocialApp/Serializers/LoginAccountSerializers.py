from rest_framework import serializers


class LoginAccountSerializer(serializers.Serializer):
    account = serializers.CharField(required=True)
    password = serializers.CharField()

