
#list methods -----------------

#The list methods are built-in functions that can be used to perform various operations on lists. Here are some commonly used list methods:
#---------------------------------------------------------------------------------------------------
#1. append() - 

# Adds an item to the end of the list.

fruits= ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits) #output: ['apple', 'banana', 'cherry', 'date']

#1.1 In the append() method, you can only add one item at a time. If you want to add multiple items, you can use the extend() method. but if you use the append() method with a list as an argument, it will add the entire list as a single item to the end of the original list.

fruits = ["apple", "banana", "cherry"]
fruits.append(["date", "fig", "grape"]) # type: ignore
print(fruits) #output: ['apple', 'banana', 'cherry', ['date', 'fig', 'grape']]

#1.2 when you use to print the length of the list it will count the entire list as one item.
print(len(fruits)) #output: 4 but at there you have 6 items in the list but it will count the entire list as one item because you have used the append() method to add the list as a single item to the original list. If you want to add multiple items from another list, you should use the extend() method instead of append().



#---------------------------------------------------------------------------------------------------


#2.extend -

# The extend() method is used to add all the items from one list to another list. It takes an iterable (like a list, tuple, or set) as an argument and adds each item from that iterable to the end of the list.
fruits = ["apple", "banana", "cherry"]
fruits.extend(["date", "fig", "grape"])
print(fruits) #output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

#2.1 In extend() method, you can add multiple items from another list, and it will add each item from that list to the end of the original list. If you use the extend() method with a list as an argument, it will add each item from that list to the end of the original list.
fruits = ["apple", "banana", "cherry"]
fruits.extend(["date", "fig", "grape"])
print(fruits) #output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

#when you use to print the length of the list it will count each item from the list as a separate item.
print(len(fruits)) #output: 6 because you have used the extend() method to add each item from the list to the original list, so it will count each item as a separate item in the list.


#3. insert() - 
 
# The insert() method is used to add an item at a specific index in the list. It takes two arguments: the index where you want to insert the item and the item itself.

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "date")
print(fruits) #output: ['apple', 'date', 'banana', 'cherry']

#3.1when you want  to insert multiple items in the list you can use the extend() method to add multiple items to the end of the list and then use the insert() method to move those items to the desired index position in the list.
fruits = ["apple", "banana", "cherry"]
fruits.extend(["date", "fig", "grape"])
fruits.insert(1, fruits[-3:]) # type: ignore
print(fruits) #output: ['apple', ['date', 'fig', 'grape'], 'banana', 'cherry', 'date', 'fig', 'grape']  
#explanation: In this example, we first use the extend() method to add multiple items to the end of the list. Then, we use the insert() method to insert those items at a specific index (in this case, index 1). The slice fruits[-3:] is used to get the last three items that were added to the list, and it is inserted as a single item at index 1. As a result, the original list now contains a nested list at index 1, which includes the three new items.

#when you use to print the length of the list it will count the entire list as one item because you have used the insert() method to add the list as a single item to the original list.
print(len(fruits)) #output: 7 but at there you have 9 items in the list but it will count the entire list as one item because you have used the insert() method to add the list as a single item to the original list. If you want to add multiple items from another list, you should use the extend() method instead of insert().

#4.remove(element) -

#  - The remove() method is used to remove the first occurrence of a specified item from the list. It takes a single argument, which is the item you want to remove.

fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits.remove("banana")
print(fruits) #output: ['apple', 'cherry', 'date', 'fig']

#when you have multiple occurrences of the item in the list, only the first occurrence will be removed.
fruits = ["apple", "banana", "cherry", "banana", "date", "fig"]
fruits.remove("banana")
print(fruits) #output: ['apple', 'cherry', 'banana', 'date', 'fig']

#when you try to remove an item that is not in the list, it will raise a ValueError.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits.remove("grape") #output: ValueError: list.remove(x): x not found

#when you want to remove two items from the list you can use the remove() method twice to remove both items from the list.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits.remove("banana")
fruits.remove("date")
print(fruits) #output: ['apple', 'cherry', 'fig']

#when you want to remove all occurrences of an item from the list, you can use a loop to iterate through the list and remove all occurrences of that item.
fruits = ["apple", "banana", "cherry", "banana", "date",
    "fig"]
while "banana" in fruits:
    fruits.remove("banana")
print(fruits) #output: ['apple', 'cherry', 'date', 'fig']



#5.pop(index) -

# The pop() method is used to remove an item at a specific index from the list and returns the removed item. It takes a single argument, which is the index of the item you want to remove.

fruits = ["apple", "banana", "cherry", "date", "fig"]
removed_item = fruits.pop(1)
print(removed_item) #output: banana
print(fruits) #output: ['apple', 'cherry', 'date', 'fig']

#when you try to pop an item at an index that is out of range, it will raise an IndexError.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits.pop(10) #output: IndexError: pop index out of range

#when you want to pop the last item from the list, you can use the pop() method without an argument, and it will remove and return the last item from the list.

fruits = ["apple", "banana", "cherry", "date", "fig"]   
removed_item = fruits.pop()
print(removed_item) #output: fig
print(fruits) #output: ['apple', 'banana', 'cherry', 'date']


#6.index -
 
#  The index() method is used to find the index of the first occurrence of a specific item in a list. It takes an item as an argument and returns the index of the first occurrence of that item in the list. If the item is not found, it raises a ValueError.
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana")) #output: 1

age = [25, 30, 35, 40]
print(age.index(35)) #output: 2
fruits = ["apple", "banana", "cherry"]
print(fruits.index("grape")) #output: ValueError: 'grape' is not in list

#when you want to find the index of all occurrences of an item in the list, you can use a loop to iterate through the list and find the index of each occurrence of that item.
fruits = ["apple", "banana", "cherry", "banana"]
item_to_find = "banana"
indices = []
for index in range(len(fruits)):
    if fruits[index] == item_to_find:
        indices.append(index)
print(indices) #output: [1, 3]


#7.count-

# The count() method is used to count the number of occurrences of a specific item in a list. It takes an item as an argument and returns the number of times that item appears in the list.
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits.count("apple")) #output: 2

age = [25, 30, 35, 40, 25]
print(age.count(25)) #output: 2


#8.sort() -

# The sort() method is used to sort the items of a list in ascending order. It modifies the original list and does not return a new list. By default, it sorts the items in ascending order, but you can also specify the sorting order using the reverse parameter.
fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits) #output: ['apple', 'banana', 'cherry']

age = [40, 25, 35, 30]
age.sort()
print(age) #output: [25, 30, 35, 40]

#9.reverse() - 

# The reverse() method is used to reverse the order of the items in a list. It modifies the original list and does not return a new list.

fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits) #output: ['cherry', 'banana', 'apple']

age = [25, 30, 35, 40]
age.reverse()
print(age) #output: [40, 35, 30, 25]

#10.clear() -

# The clear() method is used to remove all items from the list, resulting in an empty list.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits.clear()
print(fruits) #output: []

age = [25, 30, 35, 40]
age.clear()
print(age) #output: []

#11.copy() - 

# The copy() method is used to create a shallow copy of a list. It returns a new list that contains the same items as the original list. Modifying the new list will not affect the original list, and vice versa.
fruits = ["apple", "banana", "cherry"]  
fruits_copy = fruits.copy()
print(fruits_copy) #output: ['apple', 'banana', 'cherry']

# when you modify the new list, it does not affect the original list.
fruits= ["apple", "banana", "cherry"]
fruits_copy = fruits.copy()
fruits_copy.append("date")
print(fruits) #output: ['apple', 'banana', 'cherry']
print(fruits_copy) #output: ['apple', 'banana', 'cherry', 'date']

#12.sort(reverse=True) -

# The sort() method can also be used to sort the items of a list in descending order by passing the reverse=True argument. This will sort the items in reverse (descending) order.

fruits = ["banana", "apple", "cherry"]
fruits.sort(reverse=True)
print(fruits) #output: ['cherry', 'banana', 'apple']


age = [40, 25, 35, 30]
age.sort(reverse=True)
print(age) #output: [40, 35, 30, 25]

#13.sorted() - 

# The sorted() function is a built-in function that returns a new sorted list from the items in an iterable. It does not modify the original list. By default, it sorts the items in ascending order, but you can also specify the sorting order using the reverse parameter.
fruits = ["banana", "apple", "cherry"]
sorted_fruits = sorted(fruits)
print(sorted_fruits) #output: ['apple', 'banana', 'cherry']

age = [40, 25, 35, 30]
sorted_age = sorted(age)
print(sorted_age) #output: [25, 30, 35, 40]











