from rest_framework import serializers
from user.models import User


# User Serializer Class
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
