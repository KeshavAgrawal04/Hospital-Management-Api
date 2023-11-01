from rest_framework import serializers
from doctor.models import Doctor


# Doctor Serializer Class
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'