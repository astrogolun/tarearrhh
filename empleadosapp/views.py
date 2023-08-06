from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeFilterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from datetime import datetime

def signup(request):  
    
    if request.method == 'GET':
        print('Enviando formulario')
        return render(request, 'signup.html', {'form':UserCreationForm }) 
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                #return HttpResponse('Usuario creado exitosamente')
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                'form':UserCreationForm,
                "error":'El usuario ya existe'
                })
                
        return render(request, 'signup.html', {
                'form':UserCreationForm,
                "error":'Las contraseñas no coinciden'
                })    
        
        
        #print(request.POST)()
        #print('Obteniendo datos')          

def signin(request):
    template_name='signin.html'
    
    if request.method == 'GET':
        return render (request, template_name, {'form':AuthenticationForm
        })    
    
    else:
        user = authenticate(request, 
                     username=request.POST['username'], 
                     password=request.POST['password'])
    
        if user is None:
            return render (request, template_name, 
                           {'form': AuthenticationForm, 
                            'error': "Usuario o contraseña es incorrecto"
        })    
        else:
            login(request, user)
            return redirect ('home')

def home(request):
    form = EmployeeFilterForm()
    employees = Employee.objects.all()
    return render(request, 'home.html', {'form': form, 'employees': employees})
            
def vista_filtro(request):
    employees=Employee.objects.all()
    
    if request.method == 'GET':
        return render(request, 'filtro.html', 
                {'form': EmployeeFilterForm(), 'employees':employees })
    else:
        x = request.POST.get('national_id_number')
        y = request.POST.get('fecha_inicio')
        z = request.POST.get('fecha_termino')
        imprime = (x, y, z)
        
        #employees = Employee.objects.filter(nationalidnumber=x)
        #employees = Employee.objects.filter(nationalidnumber=x,hiredate__gte=y)
        employees = Employee.objects.filter(hiredate__gte=y)
        #employees = Employee.objects.filter(enddate=z)
        print(request.POST)  
        return render(request, 'filtro.html', {'form': EmployeeFilterForm(), 'employees':employees, 'print':imprime} )     
        
    #employees = Employee.objects.all()
    
    
    #empleados_filtrados = Employee.objects.filter(nationalidnumber=form.national_id_number)
    
    #return render(request, 'filtro.html', {'form': EmployeeFilterForm(), 'employees':empleados_filtrados })
 
    
