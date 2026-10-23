from abc import ABC, abstractmethod

class employee:
    def __init__(self,id,name,age,salary,dept,mobile):
        self.__id=id
        self.__name=name
        self.__age=age
        self.__salary=salary
        self.__dept=dept
        self.__mobile=mobile

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Age: {self.__age}, Salary: {self.__salary}, Department: {self.__dept}, Mobile: {self.__mobile}"

    def to_dict(self):
            return{
                "ID": self.get_id(),
                "Name":self.get_name(),
                "Age":self.get_age(),
                "Salary":self.get_salary(),
                "Department":self.get_dept(),
                "Mobile":self.get_mobile()
            }
    
    def get_all(self):
        return  [
            self.__id,
            self.__name,
            self.__age,
            self.__salary,
            self.__dept,
            self.__mobile
        ]

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_salary(self):
        return self.__salary
    def get_dept(self):
        return self.__dept
    def get_mobile(self):
        return self.__mobile
    def get_id(self):
        return self.__id


class employeeRepository(ABC):
    @abstractmethod
    def add_employee(self):
        pass

    @abstractmethod
    def read_employee(self):
        pass

    @abstractmethod
    def update_employee(self):
        pass

    @abstractmethod
    def delete_employee(self):
        pass