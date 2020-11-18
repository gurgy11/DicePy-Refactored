from . import Table
from .. import Database


class UsersTable(Table):
    
    def __init__(self):
        self.table = 'users'
        self.columns = [
            'id',
            'first_name', 'last_name',
            'email', 'phone',
            'username', 'password',
            'address_id'
            'created_at'
        ]
        self.sql_schema = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT,
            fname VARCHAR(100),
            lname VARCHAR(100),
            email VARCHAR(255),
            phone VARCHAR(25),
            username VARCHAR(100),
            password VARCHAR(255),
            address_id INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
        """
        
    def create_table(self):
        sql_schema = self.sql_schema
        self.db.create_table(sql_schema)