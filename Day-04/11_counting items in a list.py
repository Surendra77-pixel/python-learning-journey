# counting items in a list


#1. using the len() function - The len() function is used to get the number of items in a list. It takes a list as an argument and returns the number of items in that list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits)) #output: 3

age = [25, 30, 35, 40]
print(len(age)) #output: 4

#2.count method - The count() method is used to count the number of occurrences of a specific item in a list. It takes an item as an argument and returns the number of times that item appears in the list.
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits.count("apple")) #output: 2

age = [25, 30, 35, 40, 25]
print(age.count(25)) #output: 2

