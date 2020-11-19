class Supplier():
    
    def __init__(self, company_name, about, email, phone, street_address, city, postal_code, 
                 province, country, notes):
        self._id = None
        self._company_name = company_name
        self._about = about
        self._email = email
        self._phone = phone
        self._street_address = street_address
        self._city = city
        self._postal_code = postal_code
        self._province = province
        self._country = country
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
    def street_address(self):
        return self._street_address
    
    @property
    def city(self):
        return self._city
    
    @property
    def postal_code(self):
        return self._postal_code
    
    @property
    def province(self):
        return self._province
    
    @property
    def country(self):
        return self._country
    
    @property
    def notes(self):
        return self._notes
    
    @property
    def created_at(self):
        return self._created_at
    
    ''' Setters '''
    
    @id.setter
    def id(self, supplier_id):
        self._id = supplier_id
        
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
        
    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address
        
    @city.setter
    def city(self, city):
        self._city = city
        
    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code
        
    @province.setter
    def province(self, province):
        self._province = province
        
    @country.setter
    def country(self, country):
        self._country = country
        
    @notes.setter
    def notes(self, notes):
        self._notes = notes
        
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at
    
    ''' Class Methods '''
    
    def to_dict(self):
        supplier_dict = {'id': self._id, 'company_name': self._company_name, 'about': self._about, 
                         'email': self._email, 'phone': self._phone, 'street_address': self._street_address,
                         'city': self._city, 'postal_code': self._postal_code, 'province': self._province,  
                         'country': self._country, 'notes': self._notes, 'created_at': self._created_at}
        
        return supplier_dict