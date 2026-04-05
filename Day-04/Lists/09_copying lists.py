
#copying lists:


#1. using the copy() method - 
 
# The copy() method is used to create a shallow copy of a list. It returns a new list that contains the same items as the original list.

fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
print(new_fruits) #output: ['apple', 'banana', 'cherry']

#2. using the list() constructor - 

# The list() constructor can be used to create a new list that contains the same items as the original list.

fruits = ["apple", "banana", "cherry"]
new_fruits = list(fruits)
print(new_fruits) #output: ['apple', 'banana', 'cherry']

#3. using slicing - 

# Slicing can be used to create a new list that contains all the items from the original list.

fruits = ["apple", "banana", "cherry"]
new_fruits = fruits[:]
print(new_fruits) #output: ['apple', 'banana', 'cherry']