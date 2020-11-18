from ..people_model import Person


class User(Person):
    
    def __init__(self, fname, lname, email, phone, username, password, address_id):
        super().__init__(fname, lname, email, phone, address_id)
        self._id = None
        self._username = username
        self._password = password
        self._created_at = None
        
    ''' Properties and Setters '''
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
        
    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at
        
    ''' Class Methods '''
    
    def to_dict(self):
        ''' Returns a clearned dict of the user '''
        
        user_dict = {'id': self._id, 'fname': self._fname, 'lname': self._lname, 'email': self._email, 
                     'phone': self._phone, 'username': self._username, 'password': self._password, 
                     'address_id': self._address_id, 'created_at': self._created_at}
        
        return user_dict