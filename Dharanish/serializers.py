from rest_framework import serializers
from .models import Login,SignUp,NewAccount,OutpassInformation
class Loginserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Login
		fields=('EmailId','Password')


class SignUpserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=SignUp
		fields=('Fullname','PhoneNumber','RollNumber','Password')


class NewAccountserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=NewAccount
		fields=('RollNumber','Password','ConfirmPassword')


class OutpassInformationserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=OutpassInformation
		fields=('StudentName','RollNo','Department','Year','RoomNo','Reason')




	 


	















