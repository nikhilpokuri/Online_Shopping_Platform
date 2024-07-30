from abstract_order import Order
from payment_factory import factory

class Order_details:
    def __init__(self) -> None:
        self.items = []
        self.shipping_address = ""
        self.bill = 0
        self.payment_method = ""

class OrderBuilder(Order):
    def __init__(self) -> None:
        self.order = Order_details()

    def add_item(self, item):
        self.order.items.append(item)
        return self
    
    def set_shipping_address(self, address):
        self.order.shipping_address = address
        return self

    def set_bill(self, bill):
        self.order.bill = bill
        return self

    def set_payment_method(self, method):
        if factory(method, self.order.bill):
            self.order.payment_method = method
            return self
        raise Exception("Invalid Payment Mode")
    
    def make_order(self):
        return f"Order with {', '.join(self.order.items)} items, shipping to {self.order.shipping_address}"