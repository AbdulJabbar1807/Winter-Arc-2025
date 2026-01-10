class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car_1 = Car('Tata','Harrier',2500000)
car_2 = Car('Hyundai','Creta',200000)
print(car_1.brand)
print(car_1.model)
print(f'Rs.{car_1.price}')
print(car_2.brand)
print(car_2.model)
print(f'Rs.{car_2.price}')