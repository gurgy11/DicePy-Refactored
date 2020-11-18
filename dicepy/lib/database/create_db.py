from .database import Database
from .tables import *

''' Initialize table objects '''
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
    users_table.create_table()