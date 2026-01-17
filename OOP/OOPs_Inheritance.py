class Car:
    tax_rate = 0.24 # Class variable (also,24 % of total price).
    
    def __init__(self, brand, model, price):
        Car.is_price_valid(price)
        self._brand = brand # read only for immutability.
        self._model = model # read only for immutability.
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
    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

class ElectricCar(Car):
    def __init__(self, brand, model, price, battery_range):
        super().__init__(brand, model, price)
        self.battery_range = battery_range # range in KM
    def price_with_tax(self):
        base_price = super().price_with_tax()
        subsidy = 50000
        return base_price - subsidy

car_1 = ElectricCar('Tata','Harrier',3000000,700)
print(f' Battery range of Tata Harrier Ev is {car_1.battery_range} KM per full charge.')
e1 = ElectricCar("Tesla", "Model Y", 6000000, 500)

print(e1.brand)          # inherited
print(e1.price)          # inherited & encapsulated
print(e1.battery_range)  # child-specific
