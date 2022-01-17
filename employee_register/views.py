from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_list(request):
	employee_list=Employee.objects.all()
	return render(request,'employee_register/employee_list.html',{'employee_list':employee_list})

def employee_form(request,id=0):
	if request.method=="GET":

		if id==0:
			form=EmployeeForm()#new employee insertion form
		else:
			employee=Employee.objects.get(pk=id)
			form=EmployeeForm(instance=employee)#existing employee updation form
			
		return render(request,'employee_register/employee_form.html',{'form':form})    
			

	else:
		if id==0:
			form=EmployeeForm(request.POST)#put newly inserted employee data
		else:
			employee=Employee.objects.get(pk=id)
			form=EmployeeForm(request.POST,instance=employee)#put updated data
			
		if form.is_valid():
			form.save()
		return redirect('/employee/list')	
		


	
def employee_delete(request,id):
	employee=Employee.objects.get(pk=id)
	employee.delete()
	return redirect('/employee/list')	
	



