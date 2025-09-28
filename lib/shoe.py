class Shoe:
    def __init__(self, brand, size, material=None, condition="Used"):
        self.brand = brand
        self.size = size
        self.material = material
        self.condition = condition
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise ValueError("Brand must be a string")
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")  # CHANGED: print instead of raise
    
    @property
    def material(self):
        return self._material
    
    @material.setter
    def material(self, material):
        if material is None or isinstance(material, str):
            self._material = material
        else:
            raise ValueError("Material must be a string")
    
    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, condition):
        if isinstance(condition, str):
            self._condition = condition
        else:
            raise ValueError("Condition must be a string")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"