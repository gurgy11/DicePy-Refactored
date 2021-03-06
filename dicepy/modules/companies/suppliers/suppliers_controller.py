import math
from . import Supplier
from dicepy.lib.database import Database
from dicepy.lib.pagination import Paginator


class SuppliersController():
    
    def __init__(self):
        self.db = Database()
        self.table = 'suppliers'
        self.columns = ['company_name', 'about', 'email', 'phone', 'street_address', 'city', 'postal_code', 
                        'province', 'country', 'notes']
        
    def result_to_model(self, result):
        supplier = Supplier(result[1], result[2], result[3], result[4], result[5], result[6], 
                            result[7], result[8], result[9], result[10])
        return supplier
        
    def select_all(self):
        results = self.db.select_all(self.table)
        suppliers = []
        
        for res in results:
            supplier = self.result_to_model(res)
            suppliers.append(supplier)
            
        return suppliers
        
    def select_in_range(self, page, limit):
        paginator = Paginator(self.table, page, limit)
        
        all_suppliers = self.select_all()
        suppliers_in_range = paginator.select_in_range(all_suppliers)
        number_of_pages = paginator.get_number_of_pages()
        
        return suppliers_in_range, number_of_pages
    
    def company_name_exists(self, company_name):
        results = self.db.select_all_where(self.table, 'company_name', company_name)
        if len(results) > 0:
            return True
        else:
            return False
    
    def create(self, form):
        pass