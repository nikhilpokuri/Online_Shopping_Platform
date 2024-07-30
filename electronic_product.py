from abstract_products import ElectronicProducts

class Laptop(ElectronicProducts):
    def get_specification_details(self):
        return {
            "brand": "MSI",
            "model": "Model-10",
            "processor": "AMD Ryzen 5",
            "RAM": "8GB",
            "storage": "256GB SSD",
            "screen_size": "14 inches",
        }
    
    def get_mrp_details(self):
        return {"price": 69999}

class Mobile(ElectronicProducts):
    def get_specification_details(self):
        return {
            "brand": "Vivo",
            "model": "Model-11",
            "processor": "Snapdragon",
            "RAM": "6GB",
            "storage": "128GB",
            "screen_size": "14 inches",
            "battery": "5000mAh",
            "camera": "16MP",
        }
    
    def get_mrp_details(self):
        return {"price": 45999}