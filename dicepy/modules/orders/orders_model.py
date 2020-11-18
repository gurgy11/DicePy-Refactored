import datetime as dt


class Order():
    
    def __init__(self, product_id, quantity, shipping_method, order_status, shipped_at):
        self._id = None
        self._product_id = product_id
        self._quantity = quantity
        self._shipping_method = shipping_method
        self._order_status = order_status
        self._shipped_at = shipped_at
        self._created_at = dt.datetime.now()