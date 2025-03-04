from rest_framework import serializers
from emoSocialApp.models import User


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"