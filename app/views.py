from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models import Prefetch
from django.db.models import *
from django.db.models.functions import Length
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
    

def display_dept(request):
    LDO=Dept.objects.all()
    d={'LDO':LDO}
    return render(request,'display_dept.html',d)

    
def display_emp(request):
    LEO=Emp.objects.all()
    d={'LEO':LEO}
    return render(request,'display_emp.html',d)

def display_salgrade(request):
    LSO=SalGrade.objects.all()
    d={'LSO':LSO}
    return render(request,'display_salgrade.html',d)

def empToDeptjoins(request):
    LEDO=Emp.objects.select_related('deptno').all()
    LEDO=Emp.objects.select_related('deptno').filter(job='MANAGER')
    LEDO=Emp.objects.select_related('deptno').filter(sal__gt=1000)
    LEDO=Emp.objects.select_related('deptno').filter(deptno=30)
    LEDO=Emp.objects.select_related('deptno').filter(job__in=('CLERK','SALESMAN'))
    LEDO=Emp.objects.select_related('deptno').filter(ename__in=('SMITH','ALLEN'))
    LEDO=Emp.objects.select_related('deptno').filter(sal__lte=1500)
    LEDO=Emp.objects.select_related('deptno').filter(ename__contains='M')
    LEDO=Emp.objects.select_related('deptno').filter(deptno__in=(10,30))
    LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    LEDO=Emp.objects.select_related('deptno').filter(ename__startswith='S')
    LEDO=Emp.objects.select_related('deptno').filter(ename__endswith='N')
    LEDO=Emp.objects.select_related('deptno').filter(hiredate__day=16)
    LEDO=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    LEDO=Emp.objects.select_related('deptno').filter(mgr=7698)
    LEDO=Emp.objects.select_related('deptno').filter(deptno=20)
    LEDO=Emp.objects.select_related('deptno').filter(job__in=('MANAGER','SALESMAN'))
    LEDO=Emp.objects.select_related('deptno').filter(ename__in=('BLAKE','MARTIN'))
    LEDO=Emp.objects.select_related('deptno').filter(sal__gte=1500)
    LEDO=Emp.objects.select_related('deptno').filter(ename__contains='L')
    LEDO=Emp.objects.select_related('deptno').filter(deptno__in=(30,40))
    LEDO=Emp.objects.select_related('deptno').filter(ename__regex='[KL]')
    LEDO=Emp.objects.select_related('deptno').filter(ename__regex='^M')
    LEDO=Emp.objects.select_related('deptno').filter(ename__regex='\wK+\w')
    LEDO=Emp.objects.select_related('deptno').filter(ename__regex='H\Z')
    LEDO=Emp.objects.select_related('deptno').filter(ename__regex='\AK')
    LEDO=Emp.objects.select_related('deptno').filter(job__regex='K$')
    LEDO=Emp.objects.select_related('deptno').filter(deptno__dloc='NEW YORK')
   
    '''
    maxsalary=Emp.objects.select_related('deptno').aggregate(Max('sal'))
    print(maxsalary)
    minsalary=Emp.objects.select_related('deptno').aggregate(minsal=Min('sal'))['minsal']
    print(minsalary)
    avgsalary=Emp.objects.select_related('deptno').aggregate(Avg('sal'))
    print(avgsalary)
    totalsalary=Emp.objects.select_related('deptno').aggregate(Sum('sal'))
    print(totalsalary)
    empcount=Emp.objects.select_related('deptno').aggregate(Count('sal'))
    print(empcount)
    avgdeptsal=Emp.objects.select_related('deptno').filter(deptno=20).aggregate(Avg('sal'))
    print(avgdeptsal)
    avgsalalldept=Emp.objects.select_related('deptno').values('deptno').annotate(dept_avg_sal=Avg('sal'))
    print(avgsalalldept)
    '''
    LEDO=Emp.objects.select_related('deptno').annotate(name_length=Length('ename')).filter(name_length=4)

    d={'LEDO':LEDO}
    return render(request, 'empToDeptjoins.html',d)

def empToMgrJoin(request):
    LEMO=Emp.objects.select_related('mgr').all()
    LEMO=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    LEMO=Emp.objects.select_related('mgr').filter(mgr__sal__gte=3000)
    LEMO=Emp.objects.select_related('mgr').filter(mgr__empno=7698)
    d={'LEMO':LEMO}
    return render(request,'empToMgrJoin.html',d)

def empToMgrToDeptJoin(request):
    LEDMO=Emp.objects.select_related('deptno','mgr').all()
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__sal=3000)
    AS=Emp.objects.select_related('deptno','mgr').filter(ename='ADAMS').values('sal')
    adsal=AS[0]['sal']
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(sal__gt=adsal)
    d={'LEDMO':LEDMO}
    return render(request,'empToMgrToDeptJoin.html',d)

def deptToEmpJoinPR(request):
    LDEO=Dept.objects.prefetch_related('emp_set').all()
    LDEO=Dept.objects.prefetch_related('emp_set').all().filter(dname='ACCOUNTING')
    LDEO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(ename='BLAKE')))
    LDEO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(ename__in=('SMITH','ALLEN'))))
    LDEO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(sal__gt=1500)))
    d={'LDEO':LDEO}
    return render(request,'deptToEmpJoinPR.html',d)