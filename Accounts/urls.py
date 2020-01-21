from django.urls import path
from .views import *

urlpatterns = [
	path('signup/',SignUp, name='signup'),
	path('home/',home, name='home'),
	path('myaccount/',myaccount, name='myaccount'),
	path('signin/',Login, name='signin'),
	path('logout/',Logout, name='logout'),
]