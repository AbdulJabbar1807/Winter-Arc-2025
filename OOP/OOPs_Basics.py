# class Car:
#     tax_rate = 0.24 # Class variable (also,24 % of total price).
    
#     def __init__(self, brand, model, price):
#         Car.is_price_valid(price)
#         self.brand = brand
#         self.model = model
#         self.price = price
    
#     def increase_price(self,percent): # Instance variable.
#         self.price = self.price + (self.price*percent/100)
    
#     def price_with_tax(self): # Use of class variable.
#         return self.price + (self.price * Car.tax_rate)
    
#     @classmethod
#     def new_tax_rate(cls,new_rate): # Class method
        
#         if not isinstance(new_rate,(int,float)):
#             raise ValueError("Tax rate must be a number.")
#         if new_rate < 0 or new_rate > 1:
#             raise ValueError("Tax rate must be between 0 and 1.")
        
#         cls.tax_rate = new_rate
        
#     @staticmethod
#     def is_price_valid (price):
#         if not isinstance(price,(int,float)):
#             raise ValueError("Price should be in number.")
#         if price <= 0 :
#             raise ValueError("Price should be greater than zero.")
    
        
# car_1 = Car('Tata','Harrier',Car.is_price_valid(2500000))
# car_2 = Car('Hyundai','Creta',Car.is_price_valid(2000000))

# print(f'{car_1.brand} {car_1.model} Rs{car_1.price}')
# print(f'{car_2.brand} {car_2.model} Rs{car_2.price}')

# car_1.increase_price(10) # Use of Instance variable.
# print(f'Increased price for car 1 {car_1.price}')
# car_2.increase_price(20) # Use of Instance variable.
# print(f'Increased price for car 2 {car_2.price}')

# print(f'Price with tax is Rs.{car_1.price_with_tax()} for car 1.')
# print(f'Price with tax is Rs.{car_2.price_with_tax()} for car 2.')

# Car.tax_rate = 0.30 # tax_rate increased to 0.30,use of class variable.

# print(f'Price with increased tax is Rs.{car_1.price_with_tax()} for car 1.')
# print(f'Price with increased tax is Rs.{car_2.price_with_tax()} for car 2.')

# Car.new_tax_rate(0.39) # Use of class method
# print(f'New tax rate for car 1 is Rs.{car_1.price_with_tax()}')

# # Car.tax_rate = -1 # will give 0.0 .
# print(car_1.price_with_tax())
# Car.new_tax_rate(-1) # will give an error.
# print(car_1.price_with_tax())


#------------------------------------------------------------------------------------------------------------------#

class BankAccount :
    
    def __init__(self,account_holder,balance):
        BankAccount.is_balance(balance)
        self.account_holder = account_holder
        self.balance = balance
        
    @staticmethod
    def is_balance(balance):
        if not isinstance(balance,(int,float)):
            raise ValueError("Balance should be in number's.")
    
    def deposit_amount(self,amount): # Instance Method : 1.Deposit amount
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw_amount(self,wd_amount):
        if wd_amount > self.balance:
            raise ValueError("Insufficient balance.")
        else:
            self.balance = self.balance - wd_amount
        return self.balance
    
    def check_balance(self):
        return self.balance
        
    
User_1 = BankAccount('Abdul Jabbar',340)
print(User_1.withdraw_amount(45))
print(User_1.deposit_amount(456))
print(User_1.check_balance())