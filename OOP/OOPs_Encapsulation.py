class Car:
    tax_rate = 0.24 # Class variable (also,24 % of total price).
    
    def __init__(self, brand, model, price):
        Car.is_price_valid(price)
        self.brand = brand
        self.model = model
        self._price = price # Protected attributes.
    
    def increase_price(self,percent): # Instance variable.
        self._price = self._price + (self._price*percent/100)
    
    def price_with_tax(self): # Use of class variable.
        return self._price + (self._price * Car.tax_rate)
    
    @classmethod
    def new_tax_rate(cls,new_rate): # Class method
        
        if not isinstance(new_rate,(int,float)):
            raise ValueError("Tax rate must be a number.")
        if new_rate < 0 or new_rate > 1:
            raise ValueError("Tax rate must be between 0 and 1.")
        
        cls.tax_rate = new_rate
        
    @staticmethod
    def is_price_valid (price):
        if not isinstance(price,(int,float)):
            raise ValueError("Price should be in number.")
        if price <= 0 :
            raise ValueError("Price should be greater than zero.")
        
    @property # Encapsulation
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        Car.is_price_valid(value)
        self._price = value
    
        
car_1 = Car('Tata','Harrier',2500000)