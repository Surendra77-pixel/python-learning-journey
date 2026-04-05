
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

#4. using the clear() method -

#  The clear() method is used to remove all items from the list, resulting in an empty list.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits.clear()
print(fruits) #output: []



