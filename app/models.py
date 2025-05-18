from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=50, unique=True)
    dloc=models.CharField(max_length=50)

    def __str__(self):
        return str(self.deptno)

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=50)
    hiredate=models.DateField(auto_now_add=True)
    sal=models.DecimalField(max_digits=10, decimal_places=2)
    comm=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deptno=models.ForeignKey(Dept, on_delete=models.CASCADE)
    mgr=models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.ename+' '+str(self.empno)

class SalGrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=10, decimal_places=2)
    hisal=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.grade)
