from abc import ABC, abstractmethod

class ElectronicProducts(ABC):
    @abstractmethod
    def get_specification_details(self):
        pass

    @abstractmethod
    def get_mrp_details(self):
        pass

class ClothingProduct(ABC):
    @abstractmethod
    def get_material_details(self):
        pass

    @abstractmethod
    def get_mrp_details(self):
        pass
