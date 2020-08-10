from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import  forms
from django.contrib.auth import authenticate, login #,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# this form file is used to create our own form feilds and to process it to the backend


class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	firstname = forms.CharField(max_length=200)
	lastname = forms.CharField(max_length= 100)

	class Meta:# this meta will allow us to change the attributes of the parent class
		#here the create user form is going into this meta class inoder to save that to the database
		model = User # means we are going to change the user model whenever we save something in this form
		fields = ["username","firstname","lastname","email","password1","password2"]


class LoginForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username"]