from dicepy.lib.database.database import Database
from . import Address
from dicepy.lib.controller import Controller


class AddressesController(Controller):
    
    def __init__(self):
        self.db = Database()
        self.table = 'addresses'
        self.columns = ['street_address', 'city', 'postal_code', 'province', 'country']
    
    def form_to_model(self, form):
        address = Address(form.get('street_address'), form.get('city'), form.get('postal_code'),
                          form.get('province'), form.get('country'))
        
        return address
    
    def form_to_values(self, form):
        address = self.form_to_model(form)
        values = (address.street_address, address.city, address.postal_code, address.province, address.country)
        
        return values
    
    def result_to_model(self, result):
        address = Address(result[1], result[2], result[3], result[4], result[5])
        address.id = result[0]
        address.created_at = result[6]
        
        return address
    
    def select_all(self):
        results = self.db.select_all(self.table)
        addresses = []
        
        for res in results:
            address = self.result_to_model(res)
            addresses.append(address)
            
        return addresses
    
    def select_by_id(self, record_id):
        result = self.db.select_by_id(self.table, record_id)
        address = self.result_to_model(result)
        
        return address
    
    def create(self, form):
        values = self.form_to_values(form)
        
        try:
            self.db.insert_record(self.table, self.columns, values)
            print('Successfully created a new address!')
            
            return self.db.last_insert_id()
        except Exception as e:
            print('Exception thrown creating new address: ' + str(e))
            
            return None