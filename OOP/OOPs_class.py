class Employee:
    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay 
        self.raise_pay = pay + 500000*0.1
        self.email = first + '.'+last+'@company.com'
        
    def fullname(self):
        return(f"{self.first} {self.last}")

emp_1 = Employee('Abdul','Jabbar',500000)
emp_2 = Employee('Amaan','Khan',600000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.first)
print(emp_1.fullname())        
print(emp_1.raise_pay)

class Car:
    def __init__(self,vehicle_type,brand,model_name,price)-> None :
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.name = model_name
        self.price = price
        
car_1 = Car('Petrol','Audi','Q7',9200000)
car_2 = Car('Petrol','BMW','X3',7200000)
car_3 = Car('Electric','Tesla','Model Y',6000000)
car_4 = Car('Electric','Tata','Harrier EV',2500000)

print(f"Vehicle Type = {car_2.vehicle_type},Brand = {car_2.brand},Model Name = {car_2.name},Price = Rs.{car_2.price}")
print(f"Vehicle Type = {car_4.vehicle_type},Brand = {car_4.brand},Model Name = {car_4.name},Price = Rs.{car_4.price}")

        
        

