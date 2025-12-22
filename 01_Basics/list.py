# List : list is an Data srtrucure,Mutable with representing sequential data/values.
# lists 'Values' are written in [].#
sports = ['Cricket','Football','Baseball','Basketball']
print(sports)

# We can use different built-in methods for different list operations.
sports.remove('Baseball') #removes an Value from the list.
print(sports)

sports.append('Hockey') # adds a Value to the list in the end.
print(sports)

# we can use extend() method for adding the another list with multiple values in original list.
indoor_sports = ['Chess','Carrom']
sports.extend(indoor_sports)
print(sports)

popped = sports.pop() # pop() : removes last Value from the list.
print(sports) 
# pop also returns the removed element,we store removed element into a variable.
print(popped)

print(sports.insert(2,'Running'))# Adds value to prefered index into the list.

print(sports.index('Cricket')) # To the location of Value in list.

# enumerate() : this function method returns the 2 values i.e. index , Value on that list.#
for index,sport in enumerate(sports) :
    print(index,sport)
    
sports.sort()# sort the Values in ascending order
print(sports)

sports.reverse()# reverse the values in the reverse order
print(sports)

sports.sort(reverse=True)# sorts the elements in descending order
print(sports)

sorted_sports = sorted(sports)# if we dont wants to alter the original list,
# we can store the sorted list in an variable with the help of sorted() method.#
print(sorted_sports)


num = [23,32,34,54,56]
# we can use min(),max(),and sum() operations on numbers within a list.
print(min(num))
print(max(num))
print(sum(num))

# To change list to an string
sports_str = ' - '.join(sports)
print(sports_str)
# to change string to an list
course_string = 'English , Maths , Physics'
course = course_string.split(' , ')
print(course) 
print(course.index('English'))