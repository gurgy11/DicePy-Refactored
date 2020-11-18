from .. import Order


class IncomingOrder(Order):
    
    def __init__(self, product_id, quantity, shipping_method, order_status, shipped_at, received_at,
                 supplier_id, warehouse_id, localized):
        super().__init__(product_id, quantity, shipping_method, order_status, shipped_at)
        self._received_at = received_at
        self._supplier_id = supplier_id
        self._warehouse_id = warehouse_id
        self._localized = localized