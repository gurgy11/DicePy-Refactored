class Company():
    
    def __init__(self, company_name, about, email, phone, address_id, notes):
        self._id = None
        self._company_name = company_name
        self._about = about
        self._email = email
        self._phone = phone
        self._address_id = address_id
        self._notes = notes
        self._created_at = None
        
    ''' Properties '''
    
    @property
    def id(self):
        return self._id
    
    @property
    def company_name(self):
        return self._company_name
    
    @property
    def about(self):
        return self._about
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone(self):
        return self._phone
    
    @property
    def address_id(self):
        return self._address_id
    
    @property
    def notes(self):
        return self._notes
    
    @property
    def created_at(self):
        return self._created_at
    
    ''' Setters '''
    
    @id.setter
    def id(self, company_id):
        self._id = company_id
        
    @company_name.setter
    def company_name(self, company_name):
        self._company_name = company_name
        
    @about.setter
    def about(self, about):
        self._about = about
        
    @email.setter
    def email(self, email):
        self._email = email
        
    @phone.setter
    def phone(self, phone):
        self._phone = phone
        
    @address_id.setter
    def address_id(self, address_id):
        self._address_id = address_id
        
    @notes.setter
    def notes(self, notes):
        self._notes = notes
        
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at
        
    ''' Class Methods '''
    
    ''' To Dict '''
    def to_dict(self):
        company_dict = {'id': self._id, 'company_name': self._company_name, 'about': self._about,
                        'email': self._email, 'phone': self._phone, 'address_id': self._address_id,
                        'notes': self._notes, 'created_at': self._created_at}
        
        return company_dict