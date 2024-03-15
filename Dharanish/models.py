from django.db import models
class Login(models.Model):
	EmailId = models.CharField(max_length = 200)
	Password = models.CharField(max_length = 200)

class SignUp(models.Model):
	Fullname = models.CharField(max_length = 200)
	PhoneNumber = models.CharField(max_length=200)
	RollNumber = models.CharField(max_length = 200)
	Password = models.CharField(max_length = 200)
	ConfirmPassword = models.CharField(max_length = 200)

class NewAccount(models.Model):
	RollNumber = models.CharField(max_length = 200)
	Password = models.CharField(max_length = 200)
	ConfirmPassword = models.CharField(max_length = 200)	

class OutpassInformation(models.Model):
	StudentName = models.CharField(max_length=200)
	RollNo = models.CharField(max_length = 200)
	Department = models.CharField(max_length = 200)
	Year = models.CharField(max_length = 200)	
	RoomNo = models.CharField(max_length = 200)
	Reason = models.CharField(max_length = 200)	


