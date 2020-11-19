from .. import Company


class Supplier(Company):
    
    def __init__(self, company_name, about, email, phone, address_id, notes):
        super().__init__(company_name, about, email, phone, address_id, notes)