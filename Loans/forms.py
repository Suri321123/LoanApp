from django.forms import ModelForm
from Loans.models import LoanData


class LoadDataModelForm(ModelForm):
	class Meta:
		model = LoanData
		fields = ['AvailableLoans']