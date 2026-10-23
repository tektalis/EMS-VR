import mysql.connector
from models.database import employee, employeeRepository
import os
from dotenv import load_dotenv
load_dotenv()

class DatabaseDAO(employeeRepository):
    def __init__(self):
        
            self.conn=mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            self.cursor=self.conn.cursor()
        

    def get_id(self):
          query="SELECT ID from employee order by ID desc limit 1"
          self.cursor.execute(query)
          result=self.cursor.fetchone()
          if result is None:
                return "EMP001"
          last=result[0]
          number=int(last[3:])+1
          return f"EMP{number:03d}"    

    def add_employee(self,emp):
            query="INSERT INTO employee (id,name,age,salary,dept,mobile) VALUES (%s,%s,%s,%s,%s,%s)"
            values=(emp.get_all())
            self.cursor.execute(query,values)
            self.conn.commit()

    def read_one_employee(self,id):
            try:
                query='SELECT * from employee where id=%s'
                self.cursor.execute(query,(id,))
                result=self.cursor.fetchone()
                if result is None:
                    return None
                return employee(*result)
            except Exception as e:
                print(f"Error reading employee: {e}")
                return None
    
    def read_employee(self):
            query='SELECT * from employee'
            self.cursor.execute(query)
            result=self.cursor.fetchall()
            emp=[]
            for row in result:
                emp.append(employee(*row))
            return emp

    def update_employee(self,emp):
            query="UPDATE employee SET name=%s,age=%s,salary=%s,dept=%s,mobile=%s WHERE id=%s"
            values=(emp.get_name(),emp.get_age(),emp.get_salary(),emp.get_dept(),emp.get_mobile(),emp.get_id())
            self.cursor.execute(query,values)
            self.conn.commit()

    def delete_employee(self,id):
            query="DELETE  from employee where id=%s"
            self.cursor.execute(query,(id,))
            self.conn.commit()

    def close_connection(self):
        self.cursor.close()
            
        