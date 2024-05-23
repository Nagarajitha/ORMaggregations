from django.db import models

class Dept(models.Model):
     DEPTNO = models.IntegerField(primary_key=True)
     DNAME = models.CharField(max_length=100 , unique=True)
     LOC = models.CharField(max_length=100)

     def __str__(self):
          return str(self.DEPTNO)
     

class Emp(models.Model):
     EMPNO  = models.IntegerField(primary_key=True)
     ENAME = models.CharField(max_length=100)
     JOB = models.CharField(max_length=100)
      #mgr colunm has relation with same table-->Itself (thats why we mention parent table as 'self')
     MGR = models.ForeignKey('self',on_delete=models.SET_NULL, null=True, blank=True)
     #if we delete mgr in parent we dont want to delete for child instead make it null
     HIREDATE = models.DateField()
     SAL = models.DecimalField(max_digits=10,decimal_places=2)#used to take demcimal vales form user both decimal and nondecimal upto 10 digits
    
     COMM = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
     DEPTNO = models.ForeignKey(Dept,on_delete=models.CASCADE)

     def __str__(self):
          return self.ENAME

class Salgrade(models.Model):
     GRADE = models.IntegerField(primary_key=True)
     LOSAL  = models.DecimalField(max_digits=10,decimal_places=2)
     HISAL  = models.DecimalField(max_digits=10,decimal_places=2)

     def __str__(self):
          return str(self.GRADE)

