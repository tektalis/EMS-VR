# controller/employee_controller.py

from ENUMS.db import DatabaseType, Operation
from dao.database_dao import DatabaseDAO
from models.database import employeeRepository, employee
from dao.file_dao import FileDAO
from dao.collections_dao import CollectionDAO
from validator.input_validator import InputValidator
class EmployeeController:

    def __init__(self,  view):
        self.view = view

    def select_storage(self):
        storage_type = self.view.get_storage_type()

        match storage_type:
            case DatabaseType.database.value:
                self.repository = DatabaseDAO()
                self.view.show_message("You selected Database Storage")

            case DatabaseType.file.value:
                self.repository=FileDAO()
                self.view.show_message("You selected File Storage")

            case DatabaseType.collection.value:
                self.repository=CollectionDAO()
                self.view.show_message("You selected Collection Storage")

            case _:
                raise ValueError("Invalid Storage Type")

    def start(self):
        self.select_storage()

        while True:
            operation = self.view.get_operation()
            operation=operation.lower()
            match operation:
                case Operation.add.value:
                    try:
                        print("Enter details")
                        name = input("Enter name: ")
                        InputValidator.name_checker(name)
                    
                        age = int(input("Enter age: "))
                        InputValidator.age_checker(age)
                    
                        salary = float(input("Enter salary: "))
                        InputValidator.salary_checker(salary)

                        dept = input("Enter department: ")

                        mobile = input("Enter mobile: ")
                        InputValidator.mobile_checker(mobile)
                    except Exception as e:
                        print(e)
                    
                    emp=employee(self.repository.get_id(), name, age, salary, dept, mobile)
                    self.repository.add_employee(emp)
                    print("Employee Details updated successfully")



                case Operation.read.value:
                    emp=self.repository.read_employee()
                    for e in emp:
                        print(e)
                    


                
                case Operation.update.value:
                    try:
                        print("Enter Employee ID to update:")
                        id=input()
                        InputValidator.id_checker(self.repository,id)

                        emp=self.repository.read_one_employee(id)
                        name = input("Enter name: ").strip() or emp.get_name()

                        InputValidator.name_checker(name)
                        age = int(input("Enter age: ").strip() or emp.get_age())

                        InputValidator.age_checker(age)
                        salary = float(input("Enter salary: ").strip() or emp.get_salary())
                        InputValidator.salary_checker(salary)
                        dept = input("Enter department: ").strip() or emp.get_dept()
                        mobile = input("Enter mobile: ").strip() or emp.get_mobile()
                        InputValidator.mobile_checker(mobile)

                        emp=employee(id, name, age, salary, dept, mobile)
                        self.repository.update_employee(emp)
                        print("Employee details have been updated Successfully")

                    except Exception as e:
                        print(f"Error updating employee: {e}")


                case Operation.delete.value:
                    print("Enter Employee ID to delete:")
                    id=input()
                    self.repository.delete_employee(id)

                case Operation.exit.value:
                    print("Exiting Application...")
                    break

                case _:
                    print("Invalid Choice")