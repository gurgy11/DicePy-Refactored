from .database import Database
from .tables import *

''' Initialize table objects '''
addresses_table = AddressesTable()
users_table = UsersTable()
# Todo: categories
# Todo: storage_locations
# Todo: suppliers
# Todo: products
# Todo: sub_categories
# Todo: incoming_orders
# Todo: outgoing_orders
# Todo: clients
# Todo: contacts
# Todo: employees
# Todo: expenses
# Todo: notifications

def create_all_tables():
    ''' Creates all tables that don't already exist '''
    
    addresses_table.create_table()
    users_table.create_table()