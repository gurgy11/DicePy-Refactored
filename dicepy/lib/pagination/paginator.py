import math
from ..database import Database


class Paginator():
    
    db = Database()

    def __init__(self, table, page, limit, start_index=None, end_index=None):
        self._table = table
        self._page = page
        self._limit = limit
        self._start_index = start_index
        self._end_index = end_index

    ''' Properties and Setters '''

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, table):
        self._table = table

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page):
        self._page = page

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        self._limit = limit

    @property
    def start_index(self):
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        self._start_index = start_index

    @property
    def end_index(self):
        return self._end_index

    @end_index.setter
    def end_index(self, end_index):
        self._end_index = end_index

    ''' Class Methods '''

    def get_page_params(self):
        ''' Returns a dict of the page parameters '''
        
        page_params = {
            'table': self._table,
            'page': self._page,
            'limit': self._limit,
            'start_index': self._start_index,
            'end_index': self._end_index
        }
        
        return page_params
    
    def get_number_of_rows(self):
        ''' Returns the number of rows in a table '''
        
        num_rows = self.db.number_of_records(self.table)
        return num_rows
    
    def get_number_of_pages(self):
        ''' Returns the number of pages for the table '''
        
        limit = self._limit
        num_rows = self.get_number_of_rows()
        num_pages = math.ceil(num_rows / limit)
        
        return num_pages
    
    def get_start_index(self):
        ''' Sets the start index based on page and limit '''
        
        page = self._page
        limit = self._limit
        
        self._start_index = int((page - 1) * limit)
        return self._start_index
    
    def get_end_index(self):
        ''' Sets the end index based on page and limit '''
        
        page = self._page
        limit = self._limit
        
        end_index = int(page * limit)
        self._end_index = end_index
        
        return self._end_index
    
    def select_in_range(self, all_records):
        ''' Selects only the records of a table with the range of start-end index '''
        
        start_index = self.get_start_index()
        end_index = self.get_end_index()
        
        records_in_range = []
        
        in_range = False
        for record in all_records:
            if all_records.index(record) == start_index:
                in_range = True
            elif all_records.index(record) == end_index:
                in_range = False
                
            if in_range is True:
                records_in_range.append(record)
        
        return records_in_range