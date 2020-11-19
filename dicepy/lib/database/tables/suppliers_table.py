from . import Table
from .. import Database


class SuppliersTable(Table):
    
    def __init__(self):
        self.db = Database()
        self.table = 'suppliers'
        self.columns = ['id', 'company_name', 'about', 'email', 'phone', 'address_id', 'notes', 'created_at']
        self.sql_schema = """
        CREATE TABLE IF NOT EXISTS suppliers (
            id INT AUTO_INCREMENT,
            company_name VARCHAR(100) NOT NULL,
            about TEXT,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(25) NOT NULL,
            address_id INT NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
        """
        
    def create_table(self):
        sql_schema = self.sql_schema
        self.db.create_table(sql_schema)