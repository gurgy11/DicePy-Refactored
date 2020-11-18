import os

from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()


class Database():
    
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.connection = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        
    def cursor(self):
        ''' Returns a cursor for the database connection '''
        
        return self.connection.cursor()
    
    def execute_query(self, query):
        ''' Executes a query using the cursor without values '''
        
        cursor = self.cursor()
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        return results
    
    def create_table(self, sql_schema):
        ''' Using an SQL Schema, this method creates a table in your database '''
        
        try:
            cursor = self.cursor()
            cursor.execute(sql_schema)
            
            conn = self.connection
            conn.commit()
        except Exception as e:
            return e
    
    def select_all(self, table):
        ''' Selects all records from the table '''
        
        query = """SELECT * FROM {table}""".format(table=table)
        
        cursor = self.cursor()
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        data = []
        for res in results:
            data.append(res)
            
        return data
    
    def select_by_id(self, table, record_id):
        ''' Selects a single record from the table using its ID '''
        
        query = """SELECT * FROM {table} WHERE id={record_id}""".format(table=table, record_id=record_id)
        
        results = self.execute_query(query)
        data = results[0]
        
        return data
    
    def select_all_where(self, table, column, value):
        ''' Selects records from a table that satisfy a column/value condition '''
        
        query = """SELECT * FROM {table} WHERE {column}="{value}" """.format(table=table, column=column, value=value)
        
        results = self.execute_query(query)
        data = []
        
        for res in results:
            data.append(res)
            
        return data