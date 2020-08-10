from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login') #this restricts the non logged in user 
def home(request):
	context={}
	return render(request,"home.html",context)

def registerpage(request): # here we made a django default form to display the form content
	if request.user.is_authenticated: # this prevent if a already logged in user tries go to login page again
		return redirect('/home')
	else:
		form = RegisterForm() # we are passsing in the Usercreation from into our register page view to display
		context = {'form':form} # passing the form variable as a context for now

		if request.method == "POST": # sendin the post data inside the view
			form = RegisterForm(request.POST) # if a method is equal to post then we pass in the user creation form to create or
										#identify the existing user
			if form.is_valid():
				form.save() # if form is valied save the user details
				messages.success(request, 'Account Created Sucessfully')
			return redirect('/login') # need to change the login here
		else:
			form = RegisterForm()

		return render(request,'register.html',context)

def loginpage(request):
	if request.user.is_authenticated: # this prevent if a already logged in user tries go to login page again
		return redirect('/home')
	else:
		form = LoginForm()
		context = {'form':form}
		if request.method == "POST": # sendin the post data inside the view
			username = request.POST.get('username') #getting the 
			password = request.POST.get('password')

			user = authenticate(request, username =username, password = password)
			if user is not None:
				login(request, user)
				return redirect('/home')
			else:
				messages.info(request,'Username or password is incorrect')
		return render(request,'login.html',context)


def logoutpage(request):
	logout(request)
	return redirect('/login')