from django.shortcuts import render, redirect
from .models import Employee, Employeedepartmenthistory
from .forms import EmployeeFilterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.urls.exceptions import NoReverseMatch

def signup(request):  
    
    if request.method == 'GET':
        print('Enviando formulario')
        return render(request, 'signup.html', {'form':UserCreationForm }) 
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #registrar usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
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
    try:
        employees=Employee.objects.all()
        
        if request.method == 'GET':
            return render(request, 'filtro.html', 
                    {'form': EmployeeFilterForm(), 'employees':employees })
        else:
            form = EmployeeFilterForm(request.POST)
            
            if form.is_valid():
                
                    x = request.POST.get('national_id_number')
                    y = request.POST.get('fecha_inicio')
                    z = request.POST.get('fecha_termino')            
                    
                    
                    if x and y and z:               
                            employees = Employee.objects.filter(
                                nationalidnumber=x,
                                employeedepartmenthistory__startdate__gte=y,
                                employeedepartmenthistory__enddate=z
                            )
                            print(request.POST)  
                                
                    elif x and y:
                            employees = Employee.objects.filter(
                                nationalidnumber=x,
                                employeedepartmenthistory__startdate__gte=y
                                )  
                        
                    elif y and z:
                            employees = Employee.objects.filter(
                                employeedepartmenthistory__startdate__gte=y,
                                employeedepartmenthistory__enddate=z
                                )
                            
                    elif x and z:
                            employees = Employee.objects.filter(
                                nationalidnumber=x,
                                employeedepartmenthistory__enddate=z
                                )  
                        
                    elif x:
                            employees = Employee.objects.filter(
                                nationalidnumber=x
                                )
                            
                    elif y:
                            employees = Employee.objects.filter(
                                employeedepartmenthistory__startdate=y
                            )       
                    elif z: 
                            employees = Employee.objects.filter(             
                            employeedepartmenthistory__enddate=z
                                )    
                                        
                                
                    return render(request, 'filtro.html', {'form': EmployeeFilterForm(), 'employees':employees})    
            else:
                error='  El formato de la fecha debe ser YYYY-MM-DD, por ejemplo 2008-03-01'
                return render(request, 'home.html', {'form': EmployeeFilterForm(), 'employees':employees, 'error':error})  
                                                        
    except ValueError:
        employees=Employee.objects.all()
        error = "Se produjo un error de valor"
        return render(request, 'home.html', {'form': EmployeeFilterForm(), 'employees':employees, 'error': error})
                    
    except ValidationError:
        employees=Employee.objects.all()
        error = 'Ups! El formato de la fecha debe ser YYYY-MM-DD'
        return render(request, 'home.html', {'form': EmployeeFilterForm(), 'employees':employees, 'error': error})

    except NoReverseMatch:
        employees=Employee.objects.all()
        error = 'Ups! Ocurrió un error al intentar redirigir'
        return render(request, 'home.html', {'form': EmployeeFilterForm(), 'employees':employees, 'error': error})

    except Exception as e:
        employees = Employee.objects.all()
        error_ = str(e)
        return render(request, 'home.html', {'form': EmployeeFilterForm(), 'employees': employees, 'error_': error_})




