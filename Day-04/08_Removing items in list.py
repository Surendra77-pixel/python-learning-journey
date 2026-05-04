
#Removing items in list: 

#removing items from a list can be done using several methods, including the remove() method, pop() method, del statement, and clear() method. Each of these methods serves a different purpose and can be used in various scenarios to manage the contents of a list effectively.


#1. using the remove() method - The remove() method is used to remove the first occurrence of a specified item from the list. It takes a single argument, which is the item you want to remove.

#2. using the pop() method - The pop() method is used to remove an item at a specific index from the list and returns the removed item. It takes a single argument, which is the index of the item you want to remove.

#3. using the del() statement - The del statement can be used to remove an item at a specific index from the list. It does not return the removed item.

#4. using the clear() method - The clear() method is used to remove all items from the list, resulting in an empty list.

#1. using the remove() method -

#  The remove() method is used to remove the first occurrence of a specified item from the list. It takes a single argument, which is the item you want to remove.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits.remove("banana")
print(fruits) #output: ['apple', 'cherry', 'date', 'fig']

#if there are multiple occurrences of the item in the list, only the first occurrence will be removed.
fruits = ["apple", "banana", "cherry", "banana", "date", "fig"]
fruits.remove("banana")
print(fruits) #output: ['apple', 'cherry', 'banana', 'date', 'fig']


#2. using the pop() method - 

# The pop() method is used to remove an item at a specific index from the list and returns the removed item. It takes a single argument, which is the index of the item you want to remove.
fruits = ["apple", "banana", "cherry", "date", "fig"]
removed_item = fruits.pop(1)
print(removed_item) #output: banana
print(fruits) #output: ['apple', 'cherry', 'date', 'fig']

#3. using the del() statement - 

# The del statement can be used to remove an item at a specific index from the list. It does not return the removed item.
fruits = ["apple", "banana", "cherry", "date", "fig"]
del fruits[1]
print(fruits) #output: ['apple', 'cherry', 'date', 'fig']

#if you want to delete the all fruits list, you can use the del statement with the list name:
fruit = ["apple", "banana", "cherry", "date", "fig"]
del fruits
print(fruit) #output: NameError: name 'fruits' is not defined - The del statement is used to delete the entire list fruits. After the deletion, trying to access the variable fruits will result in a NameError because it is no longer defined.

#4. using the clear() method -

#  The clear() method is used to remove all items from the list, resulting in an empty list.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits.clear()
print(fruits) #output: []



