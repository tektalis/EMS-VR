# EMS-VR Employee Management System

A simple command-line Employee Management System built in Python. The application allows users to manage employee records using different storage backends: database, JSON file, or in-memory collection.

## Overview

This project demonstrates a basic layered architecture with:
- a controller layer for application flow
- DAO classes for persistence logic
- a model layer for employee data and repository abstraction
- a validation layer for input checks
- a view layer for terminal interaction

## Features

- Add employee records
- Read all employee records
- Read a single employee by ID
- Update employee details
- Delete employee records
- Select storage type at runtime
- Basic validation for names, age, salary, and mobile numbers

## Supported Storage Types

The application supports three storage modes:

1. Database
   - Uses MySQL via `mysql-connector-python`
   - Requires database credentials in environment variables

2. File
   - Stores employee records in `emp.json`
   - Uses a JSON file as the persistence layer

3. Collection
   - Stores employee records in memory as a Python list

## Project Structure

```text
EMS-VR/
├── main.py
├── emp.json
├── README.md
├── ENUMS/
│   └── db.py
├── controller/
│   └── employee_controller.py
├── dao/
│   ├── database_dao.py
│   ├── collections_dao.py
│   └── file_dao.py
├── models/
│   └── database.py
├── validator/
│   └── input_validator.py
├── views/
│   └── employee_view.py
└── .gitignore
```

## Tech Stack

- Python 3
- MySQL connector
- Python standard library (`json`, `re`, `os`)
- `python-dotenv` for environment configuration

## Requirements

Install the dependencies needed for the project:

```bash
pip install mysql-connector-python python-dotenv
```

If you plan to use the database storage mode, configure a `.env` file with values like:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=your_database
```

## How to Run

From the project root, run:

```bash
python main.py
```

## Application Flow

When the app starts:
1. The user selects a storage type.
2. The application creates the corresponding DAO object.
3. The user chooses an operation (add, read, update, delete, or exit).
4. Input is validated before saving or updating records.

## Input Validation Rules

The validator enforces the following checks:

- Name: only letters and spaces are allowed
- Age: must be greater than 18 and less than 50
- Salary: must be non-negative
- Mobile: exactly 10 digits
- Employee ID: checked against existing data when updating

## Data Model

The employee model includes:
- ID
- Name
- Age
- Salary
- Department
- Mobile

The model also includes conversion methods for JSON serialization and database insertion.

## Notes

- `emp.json` is used when the file storage mode is selected.
- The database DAO expects a table named `employee` with columns such as `id`, `name`, `age`, `salary`, `dept`, and `mobile`.
- The file-based and collection-based implementation are designed around the same repository interface, making storage switching straightforward.

## Example Usage

- Choose `Database`, `File`, or `Collection` as storage.
- Select operation `Add Employee`.
- Enter employee details when prompted.
- View the updated records by choosing `Read Employee`.

## License

This project is a simple academic/demo application and does not include a specific license file.
