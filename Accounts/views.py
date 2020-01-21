from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'home.html')

@login_required(login_url='/home')
def myaccount(request):
	return render(request,'account.html')

def Login(request):
	if request.method=="POST":
		user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			auth.login(request,user)
			current_user=request.user
			return redirect(myaccount)
		else:
			return render(request,'login.html',{'error':"Invalid Login!"})
	return render(request,'login.html')

def SignUp(request):
	if request.method=="POST":
		if request.POST['password']==request.POST['confirmpassword']:
			try:
				user=User.objects.get(username=request.POST['username'])
				return render(request,'signup.html',{'error':"username not available!"})
			except User.DoesNotExist:
				user=User.objects.create_user(username=request.POST['username'],
				password=request.POST['password'])
				auth.login(request,user)
				return redirect(myaccount)
		else:
			return render(request,'signup.html',{'error':"password not matching"})
	else:
		return render(request,'signup.html')
	return render(request,'signup.html')

def Logout(request):
	auth.logout(request)
	return redirect(home)
