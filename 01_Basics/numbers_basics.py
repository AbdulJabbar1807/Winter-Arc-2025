# Working with the Numeric data
# 1.Integer : An integer is an whole number.eg:1,2,3,32,etc.
# 2.Float : An float is an decimal number.eg:3.43,4.34,5.65,etc.
# type() : type built in method is used to know the datatypes type.
int_num = 5
print(type(int_num))
float_num = 7.54
print(type(float_num))

# Arithmetic operations- 
# Addition : +
# Substraction : -
# Multiplication : *
# Division : /
# Floor Division // : to get the whole number as answer
# Exponent : ** 
# Modulus : % #

num_1 = 32 
num_2 = 23 
num_3 = 4 
num_4 = 2
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(num_1 // num_2)
print(num_3 % num_4)
print(num_3 ** num_4)

# absolute() : built in method to get the absolute value
# round() : built in method to get the round value
num_5 = -4 ; num_6 = 4.89
print(abs(num_5))
print(round(num_6,1))

# Comparisons :
# Equal : ==
# Not Equal : !=
# Greater than : >
# Less than : <
# Greater OR Equal : >=
# Less OR Equal : <= #
print(num_1 == num_3) #will give False#

# Type_Casting : if an interger value is enveloped within an string, we can type cast it.
type_cast = '26'
type_cast = int(type_cast)
print(type_cast + num_1)