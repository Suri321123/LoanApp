from django.shortcuts import render, redirect
from Loans.models import LoanData
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from .forms import LoadDataModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/home')
def ApplyLoan(request):
	if request.method == 'POST':
		form = LoadDataModelForm(request.POST)
		if form.is_valid():
			data=request.POST['AvailableLoans']
			new=LoanData(AvailableLoans=data,user=request.user)
			new.save()
			users = LoanData.objects.all()
			return redirect(ShowLoan)
	else:
		form_class = LoadDataModelForm
	return render(request, 'applyloan.html', {
        'form': form_class,
    })

@login_required(login_url='/home')
def ShowLoan(request):
	current_user=request.user
	loans=LoanData.objects.filter(user=current_user)
	return render(request,'showloan.html',{'loans':loans})

@login_required(login_url='/home')
def ApproveLoan(request):
	current_user=request.user
	loans=LoanData.objects.all()
	if request.method=="POST":
		approvalstatus=request.POST.getlist('approvalstatus')
		for l_id in approvalstatus:
			obj = LoanData.objects.get(LoanId=int(l_id))
			obj.ApprovalStatus=True
			obj.save()
		return render(request,'approveloan.html',{'loansAll':loans})
	return render(request,'approveloan.html',{'loansAll':loans})
