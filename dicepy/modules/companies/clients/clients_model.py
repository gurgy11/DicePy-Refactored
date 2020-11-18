from .. import Company


class Client(Company):
    
    def __init__(self, company_name, email, phone, address_id, created_at):
        self._id = None
        super().__init__(company_name, email, phone, address_id, created_at)