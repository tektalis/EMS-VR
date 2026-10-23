from enum import Enum

class DatabaseType(Enum):
    database="database"
    file="file"
    collection="collection"

class Operation(Enum):
    add="add"
    read="read"
    update="update"
    delete="delete"
    exit="exit"

