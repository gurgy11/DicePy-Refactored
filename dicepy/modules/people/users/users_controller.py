from werkzeug.security import check_password_hash, generate_password_hash

from . import User
from dicepy.lib.database import Database
from dicepy.lib.controller import Controller
from dicepy.modules.auth import AuthController
from dicepy.modules.addresses import AddressesController


class UsersController():

    def __init__(self):
        self.db = Database()
        self.table = 'users'
        self.columns = ['fname', 'lname', 'email',
                        'phone', 'username', 'password', 'address_id']
        self.auth_controller = AuthController()
        self.addresses_controller = AddressesController()

    def form_to_model(self, form):
        user = User(
            form.get('fname'), form.get('lname'), form.get(
                'email'), form.get('phone'),
            form.get('address_id'), form.get('username'), form.get('password')
        )

        return user

    def form_to_values(self, form):
        values = (form.get('fname'), form.get('lname'), form.get('email'), form.get('phone'),
                  form.get('username'), generate_password_hash(form.get('password')), form.get('address_id'))

        return values
    
    def result_to_model(self, result):
        user = User(result[1], result[2], result[3], result[4], result[5], result[6], result[7])
        user.id = result[0]
        user.created_at = result[8]
        
        return user
    
    def select_by_username(self, username):
        results = self.db.select_all_where(self.table, 'username', username)
        
        if len(results) > 0:
            result = results[0]
            user = self.result_to_model(result)
            
            return user
        else:
            return None

    def username_exists(self, username):
        results = self.db.select_all_where(self.table, 'username', username)

        if len(results) > 0:
            return True
        else:
            return False

    def email_exists(self, email):
        results = self.db.select_all_where(self.table, 'email', email)

        if len(results) > 0:
            return True
        else:
            return False

    def password_valid(self, hash_password, password):
        return check_password_hash(hash_password, password)

    def register(self, user_form, address_form):
        ''' Registers a new user and inserts them into the database '''

        ''' Validate the user form '''
        errors = []

        if self.username_exists(user_form.get('username')) is True:
            error = 'The username provided is already taken!'
            errors.append(error)
        elif len(user_form.get('username')) < 6:
            error = 'The username field must be at least 6 characters long!'
            errors.append(error)

        if self.email_exists(user_form.get('email')) is True:
            error = 'The email provided is already being used by another account!'
            errors.append(error)

        if user_form.get('password') != user_form.get('confirm_password'):
            error = 'The password fields provided must match!'
            errors.append(error)
        else:
            if len(user_form.get('password')) < 6:
                error = 'The password fields must be at least 6 characters long!'
                errors.append(error)

        if len(errors) <= 0:
            ''' Create the address in the database and return its ID '''
            address_id = self.addresses_controller.create(address_form)

            ''' Create the user if the address was successfully created '''
            if address_id is not None:
                user_form['address_id'] = address_id
                user_values = self.form_to_values(user_form)
                self.db.insert_record(self.table, self.columns, user_values)
        else:
            return errors
    
    def login(self, username, password):
        user = self.select_by_username(username)
        
        ''' Validate the login form '''
        errors = []
        
        if user is None:
            error = 'The username provided does not exist!'
            errors.append(error)
        else:
            hash_password = user.password
            if check_password_hash(hash_password, password) is not True:
                error = 'The password provided is incorrect!'
                errors.append(error)
                
        if len(errors) > 0:
            return errors
        else:
            self.auth_controller.set_user_in_session(user.id, user.username)
            
    def logout(self):
        self.auth_controller.remove_user_from_session()