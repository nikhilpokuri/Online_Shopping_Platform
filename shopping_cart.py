class Cart:
    _instance = None

    @staticmethod
    def get_instance():
        if Cart._instance == None:
            Cart()
        return Cart._instance
    
    def __init__(self):
        if Cart._instance == None:
            Cart._instance = self
            Cart._instance.items = []
        else:
            raise Exception("Cannot Create Another Instance")
        
    def add_item(self, item):
        self._instance.items.append(item)
    