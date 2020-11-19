import math

from dicepy.lib.database import Database


class Controller():
    
    def __init__(self):
        self.db = Database()
        self.table = ''
        self.columns = []
    
    def form_to_model(self, form):
        ''' Converts a form into a class model '''
        
        pass
    
    def form_to_values(self, form):
        ''' Converts a form into a tuple of values for query execution '''
        
        pass
    
    def result_to_model(self, result):
        ''' Converts a MySQL result into a class model '''
        
        pass
    
    def select_all(self):
        ''' Selects all records from the table '''
        
        results = self.db.select_all(self.table)
        return results
    
    def select_by_id(self, record_id):
        ''' Selects a single record from the table using its ID '''
        
        results = self.db.select_by_id(self.table, record_id)
        return results[0]
    
    def get_number_of_rows(self):
        ''' Returns the number of rows in the database table '''
        
        num_rows = self.db.number_of_records()
        return num_rows
    
    def get_number_of_pages(self, limit):
        ''' Returns the number of pages for a table using the limit per page '''
        
        num_rows = self.get_number_of_rows()
        num_pages = math.ceil(num_rows / limit)
        return num_pages
    
    def get_start_index(self, page, limit):
        ''' Returns the starting record's index '''
        
        start_index = int((page - 1) * limit)
        return start_index
    
    def get_end_index(self, page, limit):
        ''' Returns the ending record's index '''
        
        end_index = int(page * limit)
        return end_index
    
    def create(self, form):
        ''' Creates a database table entry using the form '''
        
        pass
    
    def edit(self, form, record_id):
        ''' Edits an existing record using the form and its ID '''
        
        pass
    
    def delete(self, record_id):
        ''' Deletes a record from the database table using its ID '''
        
        pass