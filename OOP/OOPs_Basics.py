class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def increase_price(self,percent):
        self.price = self.price + (self.price*percent/100)

car_1 = Car('Tata','Harrier',2500000)
car_2 = Car('Hyundai','Creta',200000)
print(f'{car_1.brand} {car_1.model} {car_1.price}')
print(f'{car_2.brand} {car_2.model} {car_2.price}')
car_1.increase_price(10)
print(f'Increased price for car 1 {car_1.price}')
