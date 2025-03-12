from django.db import models

# Create your models here.
#ForeignKey is a field used to create a one-to-many relationship between two models.

class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50)
    department_code = models.CharField(max_length=10)

    def __str__(self):
        return self.department_name

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50)
    employee_email = models.EmailField(max_length=50)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name

