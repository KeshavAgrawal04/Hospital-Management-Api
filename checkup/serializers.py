from rest_framework import serializers
from checkup.models import CheckUp


# Checkup Serializer Class
class CheckUpSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CheckUp
        fields = '__all__'
    