from django.shortcuts import render
from .models import Employee, Employeedepartmenthistory
from datetime import datetime


def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

##seguir trabajando aquí.. funciona hasta el filtro de nationalidnumber, ahora requiero trabajar en el formato de las fechas.

def vista_filtro(request):
    if request.method == 'POST':
        national_id_number = request.POST.get('nationalidnumber', '')
        #fecha_inicio = request.POST.get('fechainicio', '')
        #fecha_termino = request.POST.get('fechatermino', '')
        
        empleados_filtrados = Employee.objects.filter(
            nationalidnumber=national_id_number,
            #employeedepartmenthistory__startdate__gte=fecha_inicio,
            #employeedepartmenthistory__enddate__lte=fecha_termino
)
        return render(request, 'filtro.html', {'employees': empleados_filtrados})

    return render(request, 'home.html')

    
    

    
    
    
    
    
    
   
    

    
