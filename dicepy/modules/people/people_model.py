class Person():
    
    def __init__(self, fname, lname, email, phone, address_id):
        self._id = None
        self._fname = fname
        self._lname = lname
        self._email = email
        self._phone = phone
        self._address_id = address_id
        self._created_at = None
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self, fname):
        self._fname = fname
        
    @property
    def lname(self):
        return self._lname
    
    @lname.setter
    def lname(self, lname):
        self._lname = lname
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
        
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        self._phone = phone
        
    @property
    def address_id(self):
        return self._address_id
    
    @address_id.setter
    def address_id(self, address_id):
        self._address_id = address_id
        
    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at 