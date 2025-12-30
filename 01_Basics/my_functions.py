def hello_func(): # def means define
    print("hello,function.")

hello_func()

def greeting_func(greeting):
    """Greeting the function."""
    return (f'{greeting} , function') # return
    
print(greeting_func("HI").lower()) #we can also use different string methods on the funtions.

def greeting_user(greeting,name="AJ"):
    return (f'{greeting} {name}')

print(greeting_user("hello"))

# working with position argument and keyword argument.
def employee_info(*args,**kwargs):
    print(args)
    print(kwargs)

employee_info('Python','Web development',name='AJ',age=27)

#also if we pass the positional arguments as a list and keyword arguments as dicionary,
# it will interpret them as a single argument.#
def employee_info_(*args,**kwargs):
    print(args)
    print(kwargs)

skills = ['python','web development']
info = {'name':'AJ','age':'27'}
employee_info_(skills,info)

# leap year code using python -
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31] # 0 at index 0 for placeholder to easily iterate over them 1 - 12 for 12 months.

def is_leap(year):
    """Return True for leap year and False for non leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 4 == 0)

print(is_leap(2019))

def days_in_month(year,month):
    """return the number of days in that month in that year."""
    if not 1<= month <= 12:
        return 'Invalid Month'
    
    if month==2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2024,2))

# ----------------------- #
#Function example#
def calculate_average(data:list) -> float :
    """To calculate the average temperature of 7 days."""
    total = 0
    count = 0
    for temp in data :
        total = total+temp
        count += 1
        
    if count == 0:
        return 0.0
    average = total/count
    return average

def check_temp(temp : float) -> str : # type: ignore
    """to check whether the outside temperature is favourable or not."""
    if temp > 35:
        return "hot outside."
    elif temp < 20:
        return "cold outside."
    elif 20 <= temp <=35:
        return "comfortable."
    
daily_temp = [35,25,8,45,5,33,28]

print(f"Average is temperature is : {calculate_average(daily_temp)}")

for temp in daily_temp:
    print(f"Today's weather is {check_temp(temp)}")



