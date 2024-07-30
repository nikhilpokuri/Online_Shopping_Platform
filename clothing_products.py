from abstract_products import ClothingProduct

class Shirt(ClothingProduct):
    def get_material_details(self):
        return {
            "brand": "Jockey",
            "sleeves": "full",
            "size": "M",
            "color": "Blue",
            "fabric": "Cotton",
        }
    
    def get_mrp_details(self):
        return {"price": 1199}

class Jeans(ClothingProduct):
    def get_material_details(self):
        return {
            "brand": "Flying Machine",
            "size": "38",
            "color": "Light Blue",
            "fabric": "Distressed Denim",
            "fit": "Tapered Fit"
        }
    
    def get_mrp_details(self):
        return {"price": 2199}