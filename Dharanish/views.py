from rest_framework import viewsets
from .serializers import Loginserializer,SignUpserializer,NewAccountserializer,OutpassInformationserializer
from .models import Login,SignUp,NewAccount,OutpassInformation
class Loginviewset(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = Loginserializer


class SignUpviewset(viewsets.ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignUpserializer


class NewAccountviewset(viewsets.ModelViewSet):
    queryset = NewAccount.objects.all()
    serializer_class = NewAccountserializer 


class OutpassInformationviewset(viewsets.ModelViewSet):
    queryset = OutpassInformation.objects.all()
    serializer_class = OutpassInformationserializer 
    











