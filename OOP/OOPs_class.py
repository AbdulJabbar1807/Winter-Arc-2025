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

