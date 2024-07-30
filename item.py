import copy

class Item:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def clone(self):
        return copy.deepcopy(self)

dummy = Item('', 0)
def create_item(name, price):
    new_item = dummy.clone()
    new_item.name = name
    new_item.price = price
    return new_item