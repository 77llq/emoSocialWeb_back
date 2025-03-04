from rest_framework import serializers


class UpdateProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    avatar_url = serializers.CharField(allow_null=True,allow_blank=True)
    signature = serializers.CharField()
    gender = serializers.CharField()
    email = serializers.EmailField()
    birthday = serializers.DateField()
    profileBp = serializers.CharField(allow_null=True,allow_blank=True)


