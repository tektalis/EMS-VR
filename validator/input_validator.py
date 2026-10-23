import re
from dao.database_dao import DatabaseDAO
from dao.collections_dao import CollectionDAO
from dao.file_dao import FileDAO
from ENUMS.db import DatabaseType
class InputValidator:
    @staticmethod
    def name_checker(name):
        if  re.search(r"[^A-Za-z ]",name):
            raise ValueError("Name contains numbers or special Characters")
        return True
        

    @staticmethod
    def age_checker(age):
        if age<=18 or age>=50:
            raise ValueError("Age limit exceeded.")
        return True

    @staticmethod
    def mobile_checker(mobile):
        if not (mobile.isdigit() and len(mobile)==10):
            raise ValueError("Mobile is containing non numeric values")
        return True

    @staticmethod
    def salary_checker(salary):
        if salary<0:
            raise ValueError("Salary is less than 0")
        return True


    def id_checker(storage, id):
        match storage:
            case DatabaseType.database.value:
                if DatabaseDAO.read_one_employee(id) is None:
                    raise ValueError("Provided ID is not in Database")
                return True
            case DatabaseType.file.value:
                if FileDAO.read_one_employee(id) is None:
                    raise ValueError("Provided ID is not in File System")
                return True
            case DatabaseType.collection.value:
                if CollectionDAO.read_one_employee(id) is None:
                    raise ValueError("Provided ID is not in Collection System")
                return True