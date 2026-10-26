
from models.database import employeeRepository, employee

class CollectionDAO(employeeRepository):
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def read_employee(self):
        return self.employees
    
    def get_id(self):
        if not self.employees:
            return "EMP001"
        last_id = self.employees[-1].get_id()
        number = int(last_id[3:]) + 1
        return f"EMP{number:03d}"

    def read_one_employee(self, emp_id):
        for emp in self.employees:
            if emp.get_id() == emp_id:
                return emp
        return None

    def update_employee(self, updated_emp):
        for i, emp in enumerate(self.employees):
            if emp.get_id() == updated_emp.get_id():
                self.employees[i] = updated_emp
                return True
        return False

   


    def delete_employee(self, emp_id):
        for emp in self.employees:
            if emp.get_id() == emp_id:
                self.employees.remove(emp)
                return True
        return False