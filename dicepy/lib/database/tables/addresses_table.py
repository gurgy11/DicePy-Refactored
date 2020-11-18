from .. import Database
from . import Table


class AddressesTable(Table):
    
    def __init__(self):
        self.db = Database()
        self.table = 'addresses'
        self.columns = ['id', 'street_address', 'city', 'postal_code', 'province', 'country', 'created_at']
        self.schema = """
        CREATE TABLE IF NOT EXISTS addresses (
            id INT AUTO_INCREMENT,
            street_address VARCHAR(255) NOT NULL,
            city VARCHAR(100) NOT NULL,
            postal_code VARCHAR(25),
            province VARCHAR(100),
            country VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
        """
        
    def create_table(self):
        schema = self.schema
        self.db.create_table(schema)