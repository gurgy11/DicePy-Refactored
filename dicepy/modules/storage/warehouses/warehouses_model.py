class Warehouse():
    
    def __init__(self, manager_id, address_id, warehouse_name, label, notes):
        self._id = None
        self._manager_id = manager_id
        self._address_id = address_id
        self._warehouse_name = warehouse_name
        self._label = label
        self._notes = notes
        self._created_at = None