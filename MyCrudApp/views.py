from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q

###For Creating a Employee Record
def CreateEmployee(request):
    form = EmployeeForm()
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-emp')
    
    context = {
        'form' : form,
    }
    
    return render(request,'HomePage.html',context)

### For Listing the Recorded Employee through Search
def SearchEmployee(request):
    
    ###employees_list = Employee.objects.all()
    search_query = ""
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    employees = Employee.objects.filter(Q(emp_name__icontains=search_query) |
                                        Q(emp_role__icontains=search_query) |
                                        Q(emp_salary__icontains=search_query)
                                        )
    context = {
        'employees' : employees,
        'search_query' : search_query,
    }
    return render(request,'EmployeeList.html',context)

### For to edit the recorded Employees Record
def EditEmployee(request,pk):
    
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
        
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect('list-emp')
        
    context = {
        'employee': employee,
        'form': form,
    }
    
    return render(request,'EmployeeEdit.html',context)

###For deleting a Record
def DeleteEmployee(request,pk):
    
    employee = Employee.objects.get(id=pk)
    
    if request.method == 'POST':
        employee.delete()
        return redirect('list-emp')
    
    context = {
        'employee' : employee,
    }
    
    return render(request,'EmployeeDelete.html',context)
        