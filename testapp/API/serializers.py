from rest_framework.serializers import ModelSerializer
from testapp.models import Registration

#Define class ModelSerializer

class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'