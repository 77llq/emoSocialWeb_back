from rest_framework import serializers


class CodeCheckSerializer(serializers.Serializer):
    retrieve_account = serializers.CharField(required=True)
    retrieve_confirm_code = serializers.CharField()
    retrieve_password = serializers.CharField()


class AccountCheckSerializer(serializers.Serializer):
    retrieve_account = serializers.CharField(required=True)