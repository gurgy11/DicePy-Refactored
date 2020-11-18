from .. import Company


class Supplier(Company):
    
    def __init__(self, company_name, email, phone, address_id, created_at=None):
        self._id = None
        super().__init__(company_name, email, phone, address_id, created_at)