# 1.reversing the list  - The reverse() method is used to reverse the order of items in a list. It modifies the original list in place.

fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits) #output: ['cherry', "banana", "apple"]    

age = [25, 30, 35, 40]
age.reverse()
print(age) #output: [40, 35, 30, 25]

# 2.other way to reverse a list is using slicing - You can also reverse a list using slicing. This method creates a new list that contains the items from the original list in reverse order.

fruits = ["apple", "banana", "cherry"]
reversed_fruits = fruits[::-1]
print(reversed_fruits) #output: ['cherry', "banana", "apple"]


age = [25, 30, 35, 40]
reversed_age = age[::-1]
print(reversed_age) #output: [40, 35, 30, 25]

# 3.using the reversed() function - The reversed() function is a built-in function that returns an iterator that accesses the given sequence in the reverse order. You can convert this iterator to a list to get the reversed list.

fruits = ["apple", "banana", "cherry"]
reversed_fruits = list(reversed(fruits))
print(reversed_fruits) #output: ['cherry', "banana", "apple"]

age = [25, 30, 35, 40]
reversed_age = list(reversed(age))
print(reversed_age) #output: [40, 35, 30, 25]