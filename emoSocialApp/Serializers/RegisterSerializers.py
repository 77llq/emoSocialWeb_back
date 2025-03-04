from rest_framework import serializers
from emoSocialApp.models import User, UserProfile


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AccountProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"