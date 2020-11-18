from dicepy.lib.database import Database


class Table():
    
    db = Database()
    table = 'table'
    columns = []
    
    def __init__(self):
        self.table = None
        self.columns = None
        self.sql_schema = None
        
    def create_table(self):
        pass