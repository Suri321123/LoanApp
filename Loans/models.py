from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class LoanData(models.Model):
	PersonalLoan = 'Personal Loan'
	HomeLoan = 'Home Loan'
	CarLoan = 'Car Loan'
	
	LoansChoices = [
        (PersonalLoan, 'Personal Loan'),
        (HomeLoan, 'Home Loan'),
        (CarLoan, 'Car Loan'),
		]
	AvailableLoans = models.CharField(
        max_length=20,
        choices=LoansChoices,
        default=PersonalLoan,
    )
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	LoanId = models.AutoField(primary_key=True)
	ApprovalStatus=models.BooleanField(default=False)
	@property
	def category_id(self):
		return self.LoanId



