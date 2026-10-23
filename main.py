from dao.database_dao import DatabaseDAO
from controller.employee_controller import EmployeeController
from views.employee_view import employeeView


class EmployeeApplication:

    def __init__(self):
        self.view = employeeView()
        self.controller = EmployeeController(self.view)

    def run(self):
        self.controller.start()


if __name__ == "__main__":

    app = EmployeeApplication()
    app.run()