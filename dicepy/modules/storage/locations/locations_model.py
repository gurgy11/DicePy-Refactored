class Location():
    
    def __init__(self, warehouse_id, available, location_label, product_id=None, product_quantity=None):
        self._id = None
        self._warehouse_id = warehouse_id
        self._available = available
        self._location_label = location_label
        self._product_id = product_id
        self._product_quantity = product_quantity
        self._created_at = None