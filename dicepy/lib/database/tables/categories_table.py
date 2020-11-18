from . import Table


class CategoriesTable(Table):
    
    def __init__(self):
        self.table = 'categories'
        self.columns = ['id', 'category_name', 'description', 'notes', 'created_at']
        self.sql_schema = """
        CREATE TABLE IF NOT EXISTS categories (
            id INT AUTO_INCREMENT,
            category_name VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
        """
        
    def create_table(self):
        sql_schema = self.sql_schema
        self.db.create_table(sql_schema)