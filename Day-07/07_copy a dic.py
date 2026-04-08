
#copying a dictionary

# We can create a copy of a dictionary using the copy() method or the dict() constructor. Here are some examples:

# 1. Using the copy() method
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
copied_dict = my_dict.copy()
print(copied_dict) #output: {'name': 'Alice', 'age': 30, 'city': 'New York'} - The copy() method creates a shallow copy of the dictionary my_dict and assigns it to copied_dict. When we print copied_dict, it shows the same key-value pairs as my_dict.


# 2. Using the dict() constructor
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
copied_dict = dict(my_dict)
print(copied_dict) #output: {'name': 'Alice', 'age': 30, 'city': 'New York'} - The dict() constructor creates a shallow copy of the dictionary my_dict and assigns it to copied_dict. When we print copied_dict, it shows the same key-value pairs as my_dict.  

# Note: Both the copy() method and the dict() constructor create a shallow copy of the dictionary, which means that if the original dictionary contains mutable objects (like lists or other dictionaries), the copied dictionary will reference the same mutable objects. If you need a deep copy (where all nested objects are also copied), you can use the deepcopy() function from the copy module.

