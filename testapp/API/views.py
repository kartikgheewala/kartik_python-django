from rest_framework import viewsets
from testapp.API.serializers import RegistrationSerializer
from testapp.models import Registration
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Define REST_API classes

class RegistrationCRUDCBV(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]