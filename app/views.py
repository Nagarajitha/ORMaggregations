from audioop import avg
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import *
# Create your views here.

def insert_dept(request):

    DEPTNO = int(input('Enter DEPTNO : '))

    DNAME = input('Enter DNAME : ')

    LOC = input('Enter LOC : ')

    QLDO= Dept.objects.get_or_create(DEPTNO=DEPTNO , DNAME =DNAME ,LOC=LOC)[0]
    QLDO.save()


    d={'QLDO':Dept.objects.all()}
    return render(request,'display_dept.html',d)


def insert_emp(request):

    DEPTNO = int(input('Enter DEPTNO : '))#foreign key

    DO =Dept.objects.filter(DEPTNO=DEPTNO)
    if DO : 
        EMPNO = int(input('Enter EMPNO : ')) #pk
        ENAME = input('Enter ENAME : ')
        JOB = input('Enter JOB : ')
        MGR = input('Enter MGR : ')

        if MGR:
            MEO=Emp.objects.get(EMPNO=int(MGR))
        else:
            MEO=None

            #MGR =int(input('Enter MGR : ')) #object 

        HIREDATE = input('Enter HIREDATE : ')
        SAL = int(input('Enter SAL : '))
        COMM = input('Enter COMM :')
        if COMM :
            COMM = int(COMM)
        else:
            COMM=None
        QLEO= Emp.objects.get_or_create(EMPNO=EMPNO , ENAME = ENAME , JOB = JOB , MGR=MEO , HIREDATE = HIREDATE,SAL=SAL,COMM =COMM , DEPTNO=DO[0])[0]
        QLEO.save()
        d={'QLEO':Emp.objects.all()}
        return render(request,'display_emp.html',d)
    else:
        return HttpResponse('Given DEPTNO is Not present in My Parent Table DEPT')



def insert_salgrade(request):
    GRADE = int(input('Enter GRADE : ') )           
    LOSAL = int(input('Enter LOSAL : '))              
    HISAL  =int(input('Enter HISAL : '))             


    QLSO= Salgrade.objects.get_or_create(GRADE=GRADE , LOSAL=LOSAL , HISAL=HISAL)[0]
    QLSO.save()

    d={'QLSO':Salgrade.objects.all()}
    return render(request,'display_salgrade.html',d)


def display_dept(request):
    
    #Departments starting with 'A'
    QLDO = Dept.objects.filter(DNAME__iregex=r'^A') 

    # Departments ending with 'ING'
    QLDO =Dept.objects.filter(DNAME__iregex=r'ING$')  
    

    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)



def display_emp(request):
    #query to fetch all employees data
    QLEO = Emp.objects.all()

    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)



def display_salgrade(request):
    #query to fetch all salgrade data
    QLSO = Salgrade.objects.all()
    d={'QLSO':QLSO}
    return render(request,'display_salgrade.html',d)



#AGGREGATE FUNCTIONS USING ORM


# --> Sysntax
#   className.objects.aggregate(keyname = aggregateFunctionName('ColumnName'))

#   where == filter
#   having == filter + annotate (annotate used for grouping and aggregations)

def display_aggregations(request):
    #find avg salary of alla employees
    QLSO = Emp.objects.aggregate(avg_sal = Avg('SAL'))['avg_sal']
    print(QLSO)

    #QLSO = Emp.objects.values('DEPTNO').annotate(GAS = Avg('SAL')).filter(GAS__gt = AS)[GAS]

    #QLSO = Emp.objects.values('DEPTNO').annotate(GAS = Avg('SAL')).filter(GAS__lte = AS)
    #print(QLSO)


    
    d={'QLSO':QLSO}
    return render(request,'display_emp.html',d)

