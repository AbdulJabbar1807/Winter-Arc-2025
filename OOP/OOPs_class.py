import datetime
my_datetime = datetime.date(2026 , 1 , 23)


class Employee:
    numOfEmps = 0
    raise_amount = 1.09
    
    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.'+ last + '@company.com'
        Employee.numOfEmps += 1
    def fullname(self):
        return(f"{self.first} {self.last}")
    def raise_pay(self):
         self.pay = int(self.pay * self.raise_amount)
         
    # Static methods
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or  day.weekday == 6 :
            return False
        return True
    

print(Employee.is_workday(my_datetime))

emp_1 = Employee('Abdul','Jabbar',500000)
emp_2 = Employee('Amaan','Khan',600000)

print(Employee.numOfEmps)
print(emp_1.email)
print(emp_2.email)
print(emp_1.first)
print(emp_1.fullname())        
print(emp_1.pay)
print(emp_2.pay)
print(Employee.raise_amount)
print(Employee.numOfEmps)

class Car:
    NumofCars = 0
    
    def __init__(self,vehicle_type,brand,model_name,price)-> None :
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.name = model_name
        self.price = price
        Car.NumofCars += 1
 
Car.NumofCars       
car_1 = Car('Petrol','Audi','Q7',9200000)
car_2 = Car('Petrol','BMW','X3',7200000)
car_3 = Car('Electric','Tesla','Model Y',6000000)
car_4 = Car('Electric','Tata','Harrier EV',2500000)

print(Car.NumofCars)
print(f"Vehicle Type = {car_2.vehicle_type},Brand = {car_2.brand},Model Name = {car_2.name},Price = Rs.{car_2.price}")
print(f"Vehicle Type = {car_4.vehicle_type},Brand = {car_4.brand},Model Name = {car_4.name},Price = Rs.{car_4.price}")

        
        

class Cricketer:
    numofPlayers = 0
    
    def __init__(self,player_name,player_type,player_team,player_runs) -> None:
        self.player_name = player_name
        self.player_type = player_type
        self.player_team = player_team
        
player_1 = Cricketer('Virat Kohli','Right hand batsmen','India',28000)
print(player_1.player_name)
print(player_1.player_type)
print(player_1.player_team)

        