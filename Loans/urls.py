from django.urls import path
from .views import *

urlpatterns = [
	path('showloan/',ShowLoan, name='showloan'),
	path('applyloan/',ApplyLoan, name='applyloan'),
	path('approveloan/',ApproveLoan, name='approveloan'),
]