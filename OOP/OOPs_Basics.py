class Car:
    tax_rate = 0.24 # Class variable (also,24 % of total price).
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def increase_price(self,percent): # Instance variable.
        self.price = self.price + (self.price*percent/100)
    
    def price_with_tax(self):
        return self.price + (self.price * Car.tax_rate)
    
        
car_1 = Car('Tata','Harrier',2500000)
car_2 = Car('Hyundai','Creta',200000)

print(f'{car_1.brand} {car_1.model} Rs{car_1.price}')
print(f'{car_2.brand} {car_2.model} Rs{car_2.price}')

car_1.increase_price(10) # Use of Instance variable.
print(f'Increased price for car 1 {car_1.price}')
car_2.increase_price(20) # Use of Instance variable.
print(f'Increased price for car 2 {car_2.price}')

print(f'Price with tax is Rs.{car_1.price_with_tax()} for car 1.')
print(f'Price with tax is Rs.{car_2.price_with_tax()} for car 2.')

Car.tax_rate = 0.30 # tax_rate increased to 0.30,use of class variable.

print(f'Price with increased tax is Rs.{car_1.price_with_tax()} for car 1.')
print(f'Price with increased tax is Rs.{car_2.price_with_tax()} for car 2.')