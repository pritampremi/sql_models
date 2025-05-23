from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def dept(request):
    deptno=int(input('enter deptno:'))
    dname=input('enter dname:')
    dloc=input('enter dloc:')

    TDO=Dept.objects.get_or_create(deptno=deptno,dname=dname,dloc=dloc)
    if TDO[1]:
        return HttpResponse('Dept created')
    else:
        return HttpResponse('Dept already present')
    
def emp(request):
    empno=int(input('enter empno:'))
    ename=input('enter ename:')
    job=input('enter job:')
    sal=float(input('enter sal:'))
    comm=input('enter comm:')
    if comm:
        comm=float(comm)
    else:
        comm=None

    deptno=int(input('enter deptno:'))
    LDO=Dept.objects.filter(deptno=deptno)
    if LDO:
        DO=LDO[0]
    else:
        return HttpResponse('deptno you provided is not present in Parent Table (Dept)')
    
    mgr=input('enter mgr:')
    if mgr:
        mgr=int(mgr)
        MO=Emp.objects.get(empno=mgr)
    else:
        MO=None

    TEO=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,sal=sal,comm=comm,deptno=DO,mgr=MO)
    if TEO[1]:
        return HttpResponse('Emp created')
    else:
        return HttpResponse('Emp alredy present')
    
def salgrade(request):
    grade=int(input('enter grade:'))
    losal=float(input('enter losal:'))
    hisal=float(input('enter hisal:'))

    TGO=SalGrade.objects.get_or_create(grade=grade,losal=losal,hisal=hisal)
    if TGO[1]:
        return HttpResponse('SalGrade created')
    else:
        return HttpResponse('SalGrade already present')

    
