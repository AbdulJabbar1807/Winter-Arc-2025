subject = 'Maths'
if subject == 'English': #used for condition check
    print("English")
elif subject == 'Maths':
    print("Maths")
else:
    print("None")
    
# and , or and no.
user = 'student'
attendance = False
if user == 'student' and attendance: 
    print("Student is present in the class.")
else:
    print("Student is absent in the class.")
    
if not attendance:
    print("Student is absent.")
else:
    print("Student is present.")

age = 19
if age > 18 and age < 65:
    print("You can drive.")
    
# is - built-in method : used for checking the variables with same values,
# but are stored as different objects in memory.
x = [34]
y = [34]
print(x == y)
print(x is y)
print(id(x))
print(id(y))

#False values-
#1.False
#2.None
#Zero of any numeric type
#Any empty sequence.for eg:'',[],()
#Any empty mapping.for eg: {if}


condition = False # same for all the above 2,3,4, and 5.
if condition:
    print('evaluated as true.')
else:
    print('evaluated as false.')