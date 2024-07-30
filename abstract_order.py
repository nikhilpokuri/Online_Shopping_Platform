from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def set_shipping_address(self, address):
        pass

    @abstractmethod
    def set_payment_method(self, method):
        pass

    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def make_order(self):
        pass