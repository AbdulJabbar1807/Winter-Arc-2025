# Regular methods : automaticaly takes the instance as the first argument.
# Class methods : Class methods uses the @classmethod decorator, which makes the method receive 
# the class itself as the first argument (usually named cls for convention),instead of an instance (self).
# Static methods : 
import datetime
my_datetime = datetime.date(2026 , 1 , 23)


class Car:
    NumofCars = 0
    raise_prices = 1.09
    def __init__(self,vehicle_type,brand,model_name,price)-> None :
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.name = model_name
        self.price = price
        Car.NumofCars += 1
    
    # Intance method
    def raise_price(self):
        self.price = int(self.price * self.raise_prices) 

# Class method
    @classmethod
    def RaiseCar_Price(cls ,prices) :
        cls.raise_prices = prices # Class method name should be same as regular methods variable.


         
Car.NumofCars       
car_1 = Car('Petrol','Audi','Q7',9200000)
car_2 = Car('Petrol','BMW','X3',7200000)
car_3 = Car('Electric','Tesla','Model Y',6000000)
car_4 = Car('Electric','Tata','Harrier EV',2500000)
car_5 = Car('Petrol','Tata','Harrier',2500000)

print(Car.NumofCars)
print(f"Vehicle Type = {car_1.vehicle_type},Brand = {car_1.brand},Model Name = {car_1.name},Old Price = Rs.{car_4.price}")

print(Car.raise_prices)
Car.RaiseCar_Price(1.15)
print(Car.raise_prices)
car_1.raise_price()
print(car_1.price)
 
print(f"Vehicle Type = {car_1.vehicle_type},Brand = {car_1.brand},Model Name = {car_1.name},New Price = Rs.{car_1.price}")


