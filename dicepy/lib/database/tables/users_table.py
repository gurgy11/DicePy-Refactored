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
            'street_address', 
            'city', 
            'postal_code', 
            'province', 
            'country',
            'created_at'
        ]
        self.sql_schema = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(255),
            phone VARCHAR(25),
            username VARCHAR(100),
            password VARCHAR(255),
            street_address VARCHAR(255),
            city VARCHAR(100),
            postal_code VARCHAR(25),
            province VARCHAR(100),
            country VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
        """
        
    def create_table(self):
        sql_schema = self.sql_schema
        self.db.create_table(sql_schema)