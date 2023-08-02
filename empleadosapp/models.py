from django.db import models

# Create your models here.


class Employee(models.Model):
     businessentityid = models.IntegerField(primary_key=True)
     nationalidnumber = models.CharField(max_length=15)
     loginid = models.CharField(max_length=256, null=True)
     jobtitle = models.CharField(max_length=50)
     birthdate = models.DateField(null=True)
     maritalstatus = models.CharField(max_length=1,null=True)
     gender = models.CharField(max_length=1, null=True)
     hiredate = models.DateField()
     salariedflag = models.BooleanField()
     vacationhours = models.SmallIntegerField()
     sickleavehours = models.SmallIntegerField()
     currentflag = models.BooleanField(null=True)
     modifieddate = models.DateTimeField(null=True)
     organizationnode = models.CharField(max_length=255,null=True)

     def __str__(self):
         return f"{self.businessentityid} - {self.nationalidnumber}"
    
     class Meta:
         db_table = 'employee'


