from .. import Company


class Client(Company):
    
    def __init__(self, company_name, about, email, phone, address_id, notes):
        super().__init__(company_name, about, email, phone, address_id, notes)
        
    def to_dict(self):
        client_dict = {'company_name': self._company_name, 'about': self._about, 'email': self._email, 
                       'phone': self._phone, 'address_id': self._address_id, 'notes': self._notes}
        return client_dict