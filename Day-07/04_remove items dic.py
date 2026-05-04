#removing items from a dictionary

# we can remove items from a dictionary using the pop() method, popitem() method, clear() method, or del statement.


#1.pop() method -

# The pop() method removes the item with the specified key and returns its value. If the key is not found, it raises a KeyError. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
removed_value = my_dict.pop("age")
print(removed_value) #output: 30 - The pop() method is called on the dictionary my_dict with the key "age" as an argument. It removes the key-value pair associated with "age" from the dictionary and returns the value, which is 30. After this operation, the dictionary my_dict will no longer contain the key "age". If we try to pop a key that does not exist in the dictionary, it will raise a KeyError. For example:
# my_dict.pop("country") # This will raise a KeyError because the key "country" is not present in the dictionary my_dict.


#2.popitem() method -

# The popitem() method removes and returns an arbitrary key-value pair from the dictionary. Since dictionaries are unordered, you cannot predict which item will be removed. Here is an example:

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
my_dict.popitem() # This will remove and return an arbitrary key-value pair from the dictionary my_dict. Since dictionaries are unordered, the specific item that is removed cannot be predicted, and it could be any of the key-value pairs in the dictionary. After calling popitem(), the dictionary will have one less key-value pair, but we cannot determine which one was removed just by looking at the code. For example, if we call popitem() on my_dict, it might remove and return ('city', 'New York'), or it might remove and return ('age', 30), or it might remove and return ('name', 'Alice'). The output will depend on which item is removed, and it cannot be determined in advance.
removed_item = my_dict.popitem()
print(removed_item) #output: ('city', 'New York') (or ('age', 30) or ('name', 'Alice')) - The popitem() method is called on the dictionary my_dict, and it removes and returns an arbitrary key-value pair from the dictionary. Since dictionaries are unordered, the specific item that is removed cannot be predicted, and it could be any of the key-value pairs in the dictionary. After calling popitem(), the dictionary will have one less key-value pair, but we cannot determine which one was removed just by looking at the code.


#3.del method -

# we can use the del statement to remove a specific key-value pair from the dictionary by specifying the key. Here is an example:

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
del my_dict["age"]
print(my_dict) #output: {'name': 'Alice', 'city': 'New York'} - The del statement is used to remove the key-value pair associated with the key "age" from the dictionary my_dict. After this operation, the dictionary will no longer contain the key "age", and when we print the dictionary, it reflects this change, showing only the remaining key-value pairs. If we try to delete a key that does not exist in the dictionary, it will raise a KeyError. For example:
# del my_dict["country"] # This will raise a KeyError because the key "country" is not present in the dictionary my_dict.


#note - if we want to delete the entire dictionary, we can use the del statement without specifying a key. Here is an example:

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
del my_dict
print(my_dict) # type: ignore #output: NameError: name 'my_dict' is not defined - The del statement is used to delete the entire dictionary my_dict. After the deletion, trying to access the variable my_dict will result in a NameError because it is no longer defined. This means that the dictionary has been completely removed from memory, and any attempt to use it will lead to an error since it does not exist anymore.


#4.clear() method -

# The clear() method removes all items from the dictionary, resulting in an empty dictionary. Here is an example:

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
my_dict.clear()
print(my_dict) #output: {} - The clear() method is called on the dictionary my _dict, which removes all key-value pairs from the dictionary. After calling clear(), the dictionary becomes empty, and when printed, it shows as an empty dictionary {}. The variable my_dict still exists and is defined, but it does not contain any items. If we try to access any key in my_dict after clearing it, it will return None or raise a KeyError since there are no key-value pairs left in the dictionary.



