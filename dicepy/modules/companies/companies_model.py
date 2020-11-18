class Company():
    
    def __init__(self, company_name, email, phone, address_id, created_at=None):
        self._id = None
        self._company_name = company_name
        self._email = email
        self._phone = phone
        self._address_id = address_id
        self._created_at = created_at