
#sets-

#The sets are used to store multiple items in a single variable. A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets{}.

#The set items are unchangable but you can remove items and add new items to a set. The set is unordered, so you cannot be sure in which order the items will appear.

#If there are any duplicate values it removes automatically 

#sets are mutable - you can add or remove items from a set, but you cannot change the items themselves. This means that you can add new items to a set or remove existing items, but you cannot modify the value of an existing item in the set.

# the + operator is not supported for sets because sets are unordered collections of unique items, and the + operator is typically used for concatenating ordered sequences like lists or tuples. Since sets do not maintain a specific order and do not allow duplicate values, using the + operator to combine two sets would not make sense in terms of how sets are designed to function. Instead, you can use the union() method or the | operator to combine two sets while ensuring that the resulting set contains only unique items. For example:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
combined_set = set1.union(set2)  # Using the union() method
print(combined_set)  # Output: {1, 2, 3, 4, 5}

#rules in sets -------------------------------------

#1.a set will have unique values - a set cannot contain duplicate values. If you try to add a duplicate value to a set, it will be ignored and the set will remain unchanged.

#2.no indexing and slicing in sets because they are unordered and unindexed. 

#3.no order in sets - the items in a set do not have a defined order, and they cannot be accessed using an index. When you print a set, the order of the items may appear random and can change each time you run the program.

#4.mutable - you can add or remove items from a set, but you cannot change the items themselves. This means that you can add new items to a set or remove existing items, but you cannot modify the value of an existing item in the set.
 
#5.only immutable data types can be added to a set - since sets are mutable, they can only contain immutable data types such as numbers, strings, and tuples. You cannot add mutable data types such as lists or dictionaries to a set because they can be modified after they are added to the set, which would violate the immutability requirement of the items in a set.example:

my_set = {1, "hello", (1, 2, 3)}
print(my_set) #output: {1, 'hello', (1, 2, 3)} - The set my_set contains an integer, a string, and a tuple, which are all immutable data types. If you try to add a mutable data type such as a list or a dictionary to the set, you will get a TypeError because they cannot be added to a set. For example: 

my_set = {1, "hello", (1, 2, 3)}
my_set.add([4, 5, 6]) # This will raise a TypeError because lists are mutable and cannot be added to a set.


#6.finnaly remember this {}-this empty is not a set but a dictionary. To create an empty set, you need to use the set() constructor. Here is an example:
my_set = set()
print(my_set) #output: set() - The set() constructor is used to create an empty set, which is represented as set() when printed. If you try to create an empty set using {}, it will create an empty dictionary instead, which is not the same as an empty set. For example:

my_set = {}
print(my_set) #output: {} - The {} syntax creates an empty dictionary, not an empty set. To create an empty set, you should use the set() constructor as shown in the previous example.


#examples of sets -------------------------------------

#1.membership in sets - we can use the in keyword to check if an item is present in a set. Here is an example:
my_set = {1, "hello", (1, 2, 3)}
print(1 in my_set) #output: True - The in keyword checks if the item 1 is present in the set my_set and returns True because it is found in the set.

#2.when you try to create a set constructor with strings - when you create a set using the set() constructor with a string, it will create a set of individual characters from the string. Here is an example:
my_string = "hello"
my_set = set(my_string)
print(my_set) #output: {'h', 'e', 'l', 'o'} - The set() constructor takes the string "hello" and creates a set of individual characters from the string. Since sets do not allow duplicate values, the character 'l' appears only once in the set, resulting in the set {'h', 'e', 'l', 'o'}.


#3.creating a set - we can create a set using curly braces{}- 
my_set = {1, "hello", (1, 2, 3)}
print(my_set) #output: {1, 'hello', (1, 2, 3)} - The set my_set is created using curly braces {} and contains an integer, a string, and a tuple. When printed, the order of the items in the set may appear random because sets are unordered collections.

#4.tuple length - we can use the len() function to get the length of the set:
my_set = {1, "hello", (1, 2, 3)}
print(len(my_set)) #output: 3 - The len() function returns the number of unique items in the set my_set, which is 3 because it contains the integer 1, the string "hello", and the tuple (1, 2, 3). Even though the string "hello" contains multiple characters, it is treated as a single item in the set, resulting in a total of 3 unique items in the set.

#5.type() function to check the type of the set:
my_set = {1, "hello", (1, 2, 3)}
print(type(my_set)) #output: <class 'set'> - The type() function is used to check the type of the variable my_set, which is a set. The output <class 'set'> indicates that my_set is indeed a set object in Python.

#6.set constructor - we can use the set() constructor to create a set from an iterable (like a string, list, or another set):
my_string = "hello"
my_set = set(my_string)
print(my_set) #output: {'h', 'e', 'l', 'o'}

#7.creating the set with data types - we can create a set with different data types, such as integers, strings, and tuples:
my_set = {"Apple", "banana", "cherry"}
my_set2 = {1, 2, 3, 4}
my_set3 = {(1, 2), (3, 4), (5, 6)}
print(my_set) #output: {'Apple', 'banana', 'cherry'}
print(my_set2) #output: {1, 2, 3, 4}
print(my_set3) #output: {(1, 2), (3, 4), (5, 6)} - The sets my_set, my_set2, and my_set3 contain different data types, including strings, integers, and tuples. When printed, the order of the items in each set may appear random because sets are unordered collections.



