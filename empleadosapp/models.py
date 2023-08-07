from django.db import models

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


class Department(models.Model):
    departmentid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    groupname = models.CharField(max_length=50, blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'

class Shift(models.Model):
    shiftid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    starttime = models.TimeField(blank=True, null=True)
    endtime = models.TimeField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shift'

class Employeedepartmenthistory(models.Model):
    employeedepartmenthistoryid = models.AutoField(primary_key=True)
    businessentityid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='businessentityid', blank=True, null=True)
    departmentid = models.ForeignKey(Department, models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    shiftid = models.ForeignKey('Shift', models.DO_NOTHING, db_column='shiftid', blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employeedepartmenthistory'