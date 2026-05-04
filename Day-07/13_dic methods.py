
#dictionary methods

#1.keys() method -

#  The keys() method returns a view object that displays a list of all the keys in the dictionary. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
keys_view = my_dict.keys()
print(keys_view) #output: dict_keys(['name', 'age', 'city']) - The keys() method returns a view object that contains the keys of the dictionary my_dict. When we print keys_view, it shows the keys in the form of a dict_keys object, which is a view of the keys in the dictionary.

#2,values() method -

# The values() method returns a view object that displays a list of all the values in the dictionary. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
values_view = my_dict.values()
print(values_view) #output: dict_values(['Alice', 30, 'New York']) - The values() method returns a view object that contains the values of the dictionary my_dict. When we print values_view, it shows the values in the form of a dict_values object, which is a view of the values in the dictionary.


#3.items() method -

# The items() method returns a view object that displays a list of all the key:value pairs in the dictionary as tuples. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
items_view = my_dict.items()
print(items_view) #output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')]) - The items() method returns a view object that contains the key-value pairs of the dictionary my_dict as tuples. When we print items_view, it shows the key-value pairs in the form of a dict_items object, which is a view of the items in the dictionary.


# We can also use a for loop to iterate over the keys, values, or items of a dictionary. Here are some examples:
# Iterating over Keys
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
for key in my_dict.keys():
    print(key) #output: name age city - The for loop iterates over the keys of the dictionary my_dict using the keys() method, and prints each key on a new line.

# Iterating over Values
for value in my_dict.values():
    print(value) #output: Alice 30 New York - The for loop iterates over the values of the dictionary my_dict using the values() method, and prints each value on a new line.

# Iterating over Items
for key, value in my_dict.items():
    print(key, value) #output: name Alice age 30 city New York - The for loop iterates over the items of the dictionary my_dict using the items() method, and prints each key-value pair on a new line.



#4.get() method -

# The get() method returns the value of the specified key if the key is in the dictionary. If the key is not found, it returns None (or a specified default value). Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict.get("name")) #output: Alice - The get() method is called with the key "name" as an argument. Since "name" is present in the dictionary my_dict, it returns the corresponding value "Alice".


#5.update() method -

# The update() method is used to update the dictionary with the elements from another dictionary object or from an iterable of key-value pairs. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30
}
new_data = {
    "city": "New York",
    "country": "USA"
}
my_dict.update(new_data)
print(my_dict) #output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'} - The update() method is called on the dictionary my_dict with new_data as an argument. This adds the key-value pairs from new_data to my_dict. When we print my_dict, it shows the updated dictionary with all the key-value pairs from both dictionaries.


#6.pop() method -

# The pop() method removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError (or returns a specified default value). Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
removed_value = my_dict.pop("age")
print(removed_value) #output: 30 - The pop() method is called with the key "age" as an argument. Since "age" is present in the dictionary my_dict, it removes the key-value pair for "age" and returns the corresponding value, which is 30. When we print removed_value, it shows the value that was removed from the dictionary.
print(my_dict) #output: {'name': 'Alice', 'city': 'New York'} - After the pop() method is called, the key-value pair for "age" is removed from the dictionary my_dict. When we print my_dict, it shows the updated dictionary without the "age" key-value pair.

#7.popitem() method -

# The popitem() method removes and returns an arbitrary key-value pair from the dictionary. Since dictionaries are unordered, you cannot predict which item will be removed. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
removed_item = my_dict.popitem()
print(removed_item) #output: ('city', 'New York') (or ('age', 30) or ('name', 'Alice')) - The popitem() dosent take any argument 


#8.clear() method -

# The clear() method removes all items from the dictionary, resulting in an empty dictionary. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
my_dict.clear()
print(my_dict) #output: {} - The clear() method is called on the dictionary my_dict, which removes all key-value pairs from the dictionary. After calling clear(), the dictionary becomes empty, and when we print it, it shows as an empty dictionary {}.


#9.copy() method -

# The copy() method returns a shallow copy of the dictionary. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
copied_dict = my_dict.copy()
print(copied_dict) #output: {'name': 'Alice', 'age': 30, 'city': 'New York'} - The copy() method creates a shallow copy of the dictionary my_dict and assigns it to copied_dict. When we print copied_dict, it shows the same key-value pairs as my_dict, indicating that it is a copy of the original dictionary. However, since it is a shallow copy, if there are any mutable objects (like lists or other dictionaries) as values in the original dictionary, they will be shared between the original and the copied dictionary.


#10.fromkeys() method -

# The fromkeys() method creates a new dictionary with the specified keys and a common value. Here is an example:
keys = ["name", "age", "city"]
value = "Unknown"
new_dict = dict.fromkeys(keys, value)
print(new_dict) #output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'} - The fromkeys() method is called with a list of keys and a common value. It creates a new dictionary where each key from the list is associated with the specified value "Unknown". When we print new_dict, it shows the newly created dictionary with the keys and their corresponding values.


#11.setdefault() method -

# The setdefault() method returns the value of the specified key if the key is in the dictionary. If the key is not found, it inserts the key with a specified value and returns that value. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30
}
print(my_dict.setdefault("name", "Unknown")) #output: Alice - The setdefault() method is called with the key "name" and a default value "Unknown". Since "name" is already present in the dictionary my_dict, it returns the existing value "Alice" and does not change the dictionary.
print(my_dict.setdefault("city", "Unknown")) #output: Unknown - The setdefault() method is called with the key "city" and a default value "Unknown". Since "city" is not present in the dictionary my_dict, it adds the key "city" with the value "Unknown" to the dictionary and returns "Unknown". After this operation, the dictionary my_dict will now include the new key-value pair for "city". When we print my_dict, it will show the updated dictionary with the new key-value pair