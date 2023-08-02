from django.shortcuts import render
from .models import Employee
from .forms import EmployeeFilterForm

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})




