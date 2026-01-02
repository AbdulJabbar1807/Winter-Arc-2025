class Employee:
    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.'+last+'@company.com'

emp_1 = Employee('Abdul','Jabbar','500000')
emp_2 = Employee('Amaan','Khan','600000')

print(emp_1.email)
print(emp_2.email)
print(emp_1.first)
        
#Instance contain that data that are unique
