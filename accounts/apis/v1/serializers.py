from rest_framework import serializers
from accounts.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ["id", "username", "first_name", "last_name", "role", "last_login"]