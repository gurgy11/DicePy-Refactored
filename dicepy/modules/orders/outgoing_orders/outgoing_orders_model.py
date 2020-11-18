from .. import Order


class OutgoingOrder(Order):
    
    def __init__(self, product_id, quantity, shipping_method, order_status, shipped_at, 
                 delivered_at, accepted_at, warehouse_id, location_id):
        super().__init__(product_id, quantity, shipping_method, order_status, shipped_at)
        self._delivered_at = delivered_at
        self._accepted_at = accepted_at
        self._warehouse_id = warehouse_id
        self._location_id = location_id