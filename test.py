class StringValue:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, instance, value):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if type(value) is str and self.min <= len(value) <= self.max:
            instance.__dict__[self.name] = value
    
class PriceValue:
    def __init__(self, max):
        self.max = max
        
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, instance, value):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if type(value) is (int, float) and 0 <= value <= self.max:
            instance.__dict__[self.name] = value
    
class SuperShop:
    def __init__(self, name: str):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.product = product
        return self.goods.append(self.product)

    def remove_product(product):
        return self.goods.remove(self.product)

class Product:
    name = StringValue(2, 50)
    price = PriceValue(1000)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        
shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")