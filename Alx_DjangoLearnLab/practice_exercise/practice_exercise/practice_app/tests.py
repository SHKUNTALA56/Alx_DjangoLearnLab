from django.test import TestCase
from practice_app.models import Departments, Employees

# filepath: /home/deelan/Alx_DjangoLearnLab/practice_exercise/practice_app/test_models.py

class EmployeesModelTest(TestCase):
    def setUp(self):
        self.department = Departments.objects.create(
            department_name="HR",
            department_code="HR01"
        )
        self.employee = Employees.objects.create(
            employee_name="John Doe",
            employee_email="john.doe@example.com",
            department=self.department
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.employee_name, "John Doe")
        self.assertEqual(self.employee.employee_email, "john.doe@example.com")
        self.assertEqual(self.employee.department.department_name, "HR")

    def test_employee_str(self):
        self.assertEqual(str(self.employee), "John Doe")