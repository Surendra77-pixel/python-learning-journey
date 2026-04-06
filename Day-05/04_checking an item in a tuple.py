
#checking an item in a tuple -

#1. using the in operator -
#  we can use the in operator to check if an item exists in a tuple. The in operator returns True if the item is found in the tuple and False otherwise. Here is an example:

my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple) #output: True - The in operator checks if the item 3 is present in the tuple my_tuple and returns True because it is found in the tuple.
print(6 in my_tuple) #output: False - The in operator checks if the item 6 is present in the tuple my_tuple and returns False because it is not found in the tuple.

#2. using the not in operator - we can also use the not in operator to check if an item does not exist in a tuple. The not in operator returns True if the item is not found in the tuple and False otherwise. Here is an example:

my_tuple = (1, 2, 3, 4, 5)
print(6 not in my_tuple) #output: True - The not in operator checks if the item 6 is not present in the tuple my_tuple and returns True because it is not found in the tuple.
print(3 not in my_tuple) #output: False - The not in operator checks if the item 3 is not present in the tuple my_tuple and returns False because it is found in the tuple.

#3. using the index() method - we can also use the index() method to check if an item exists in a tuple. The index() method returns the index of the first occurrence of the item in the tuple. If the item is not found, it raises a ValueError. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
try:
    index = my_tuple.index(3)
    print(f"Item 3 found at index: {index}") #output: Item 3 found at index: 2 - The index() method finds the item 3 in the tuple my_tuple and returns its index, which is 2.
except ValueError:
    print("Item 3 not found in the tuple.")
try:
    index = my_tuple.index(6)
    print(f"Item 6 found at index: {index}")
except ValueError:
    print("Item 6 not found in the tuple.") #output: Item 6 not found in the tuple. - The index() method raises a ValueError because the item 6 is not found in the tuple my_tuple, and the except block catches the exception and prints a message indicating that the item is not found.

#4. using the count() method - we can also use the count() method to check if an item exists in a tuple. The count() method returns the number of occurrences of the item in the tuple. If the item is not found, it returns 0. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.count(3)) #output: 1 - The count() method counts the number of occurrences of the item 3 in the tuple my_tuple and returns 1 because it is found once in the tuple.
print(my_tuple.count(6)) #output: 0 - The count() method counts the number of occurrences of the item 6 in the tuple my_tuple and returns 0 because it is not found in the tuple.

#5.by using the if in the simple way-

list1 = [1, 2, 3, 4, 5]
if 3 in list1:
    print("Item 3 is present in the list.") #output: Item 3 is present in the list. - The if statement checks if the item 3 is present in the list list1 using the in operator, and since it is found, it executes the print statement.
if 6 in list1:
    print("Item 6 is present in the list.")
else:
    print("Item 6 is not present in the list.") #output: Item 6 is not present in the list. - The if statement checks if the item 6 is present in the list list1 using the in operator, and since it is not found, it executes the else block and prints a message indicating that the item is not present in the list.


#6,using index and count together -
my_tuple = (1, 2, 3, 4, 5)
if my_tuple.count(3) > 0:
    index = my_tuple.index(3)
    print(f"Item 3 found at index: {index}") #output: Item 3 found at index: 2 - The if statement checks if the count of the item 3 in the tuple my_tuple is greater than 0, which means it is present in the tuple. Since it is found, it retrieves the index of the first occurrence of the item using the index() method and prints a message indicating that the item is found along with its index.    


