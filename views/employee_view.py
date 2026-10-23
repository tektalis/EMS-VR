class employeeView:
    def show_welcome(self):
        print("\nWelcome to Employee Management System\n")

    def get_storage_type(self):
        print("\nChoose storage type:")
        print("Database")
        print("File")
        print("Collection")
        return input("Enter storageType: ").lower()

    def get_operation(self):
        print("\nChoose Employee:")
        print("1. Add Employee")
        print("2. Read Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        return (input("Enter operation: "))

    def show_message(self, message):
        print(message)