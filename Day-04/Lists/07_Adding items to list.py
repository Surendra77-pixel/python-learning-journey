#Adding the items to the list:
#1. using the append() method - The append() method is used to add an item to the end of the list. It takes a single argument, which is the item you want to add.

#2. using the insert() method - The insert() method is used to add an item at a specific position in the list. It takes two arguments: the index where you want to insert the item and the item itself.

#3. using the extend() method - The extend() method is used to add multiple items to the end of the list. It takes an iterable (such as another list) as an argument and adds each item from that iterable to the end of the list.

#4. using the + operator - You can also use the + operator to concatenate two lists, which creates a new list that contains all the items from both lists.

# 1. using the append() method - The append() method is used to add an item to the end of the list. It takes a single argument, which is the item you want to add.
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits) #output: ['apple', 'banana', 'cherry', 'date']


#2. using the insert() method - The insert() method is used to add an item at a specific position in the list. It takes two arguments: the index where you want to insert the item and the item itself.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "date")
print(fruits) #output: ['apple', 'date', 'banana', 'cherry']    

#3. using the extend() method - The extend() method is used to add multiple items to the end of the list. It takes an iterable (such as another list) as an argument and adds each item from that iterable to the end of the list.
fruits = ["apple", "banana", "cherry"]
fruits.extend(["date", "fig", "grape"])
print(fruits) #output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

fruits = ["apple", "banana", "cherry"]
match = ["date", "fig", "grape"]
fruits.extend(match)
print(fruits) #output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

#4. using the + operator - You can also use the + operator to concatenate two lists, which creates a new list that contains all the items from both lists.
fruits = ["apple", "banana", "cherry"]
more_fruits = ["date", "fig", "grape"]
fruits = fruits + more_fruits
print(fruits) #output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
