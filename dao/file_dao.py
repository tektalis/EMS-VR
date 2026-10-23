import json
from models.database import employeeRepository, employee
class FileDAO(employeeRepository):

    def __init__(self, file_path='emp.json'):
        self.file_path = file_path

    def _load_data(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def read_employee(self):
        employees = []
        data = self._load_data()
        for row in data:
            employees.append(employee(*row.values()))
        return employees

    def add_employee(self, emp):
        data = self._load_data()
        data.append(emp.to_dict())
        self._save_data(data)

    def get_id(self):
        data = self._load_data()
        if not data:
            return "EMP001"
        last_id = data[-1]["ID"]
        number = int(last_id[3:]) + 1
        return f"EMP{number:03d}"

    def read_one_employee(self, emp_id):
        data = self._load_data()
        for emp in data:
            if emp["ID"] == emp_id:
                return emp
        return None

    def update_employee(self, emp):
        data = self._load_data()
        for i, ex in enumerate(data):
            if ex["ID"] == emp.get_id():
                data[i] = emp.to_dict()
                self._save_data(data)
                return True
        return False

    def delete_employee(self, emp_id):
        data = self._load_data()
        new_data = [emp for emp in data if emp["ID"] != emp_id]
        if len(new_data) != len(data):
            self._save_data(new_data)
            return True
        return False

    