from dicepy.modules.addresses import addresses_controller
import math

from . import Client
from dicepy.lib.database import Database
from dicepy.lib.pagination import Paginator
from dicepy.modules.addresses import AddressesController


''' Controller for the Clients module '''
class ClientsController():
    
    def __init__(self):
        self.db = Database()
        self.table = 'clients'
        self.columns = ['company_name', 'about', 'email', 'phone', 'address_id', 'notes']
        self.addresses_controller = AddressesController()
    
    def form_to_model(self, form):
        client = Client(form.get('company_name'), form.get('about'), form.get('email'), form.get('phone'),
                        form.get('address_id'), form.get('notes'))
        return client
    
    def form_to_values(self, form):
        client = self.form_to_model(form)
        values = (client.company_name, client.about, client.email, client.phone, client.address_id, 
                  client.notes)
        
        return values
    
    def result_to_model(self, result):
        client = Client(result[1], result[2], result[3], result[4], result[5], result[6])
        client.id = result[0]
        client.created_at = result[7]
        
        return client
    
    def select_all(self):
        results = self.db.select_all(self.table)
        clients = []
        
        for res in results:
            client = self.result_to_model(res)
            clients.append(client)
        
        return clients
    
    def select_by_id(self, client_id):
        result = self.db.select_by_id(self.table, client_id)
        client = self.result_to_model(result)
        
        return client
    
    def select_in_range(self, page, limit):
        paginator = Paginator(self.table, page, limit)
        
        all_clients = self.select_all()
        clients_in_range = paginator.select_in_range(all_clients)
        
        return clients_in_range
    
    def get_number_of_pages(self, limit):
        num_rows = self.db.number_of_records(self.table)
        num_pages = math.ceil(num_rows / limit)
        
        return num_pages
    
    def company_name_exists(self, company_name):
        results = self.db.select_all_where(self.table, 'company_name', company_name)
        
        if len(results) > 0:
            return True
        else:
            return False
        
    def company_name_valid(self, company_name):
        results = self.db.select_all_where(self.table, 'company_name', company_name)
        
        if len(results) <= 1:
            return True
        else:
            return False
        
    def create(self, client_form, address_form):
        address = self.addresses_controller.search(address_form)
        address_id = None
        
        if address is None:
            address_id = self.addresses_controller.create(address_form)
        else:
            address_id = address.id
            
        errors = []    
        
        if self.company_name_exists(client_form.get('company_name')) is True:
            error = 'The company name provided is already taken!'
            errors.append(error)
        else:
            client_form['address_id'] = address_id
            values = self.form_to_values(client_form)
            try:
                self.db.insert_record(self.table, self.columns, values)
                print('Successfully created a new client record in the database!')
            except Exception as e:
                print('Exception thrown while creating a new client entry: ' + str(e))
                errors.append(str(e))
        
        return errors
    
    def edit(self, client_form, address_form, client_id):
        address = self.addresses_controller.search(address_form)
        address_id = None
        
        if address is None:
            address_id = self.addresses_controller.create(address_form)
        else:
            address_id = address.id
            
        errors = []
        
        try:
            client_form['address_id'] = address_id
            values = self.form_to_values(client_form)
            self.db.update_record(self.table, self.columns, values, client_id)
            print('Successfully updated a client record in the database!')
        except Exception as e:
            print('Exception thrown while updating a client entry in the database: ' + str(e))
            errors.append(str(e))
                
        return errors
    
    def delete(self, client_id):
        try:
            self.db.delete_record(self.table, client_id)
            print('Successfully deleted a client record from the database!')
        except Exception as e:
            print('Exception thrown while deleteing a client record from the database: ' + str(e))