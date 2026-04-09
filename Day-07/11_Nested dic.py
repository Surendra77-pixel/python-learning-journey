
#nested dictionaries - A dictionary can contain another dictionary as a value, which is known as a nested dictionary. This allows us to create more complex data structures. Here is an example of a nested dictionary:
my_dict = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}
print(my_dict) #output: {'name': 'Alice', 'age': 30, 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}} - The dictionary my_dict contains a nested dictionary under the key "address". When we print my_dict, it shows the entire structure, including the nested dictionary with its own key-value pairs.

# We can access the values in a nested dictionary by using multiple keys. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}
street = my_dict["address"]["street"]
print(street) #output: 123 Main St - To access the value of the "street" key in the nested dictionary under "address", we use my_dict["address"]["street"]. This retrieves the value "123 Main St" and assigns it to the variable street, which is then printed.


# We can also add items to a nested dictionary. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}

my_dict["address"]["zip_code"] = "10001"
print(my_dict) #output: {'name': 'Alice', 'age': 30, 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY', 'zip_code': '10001'}} - A new key-value pair is added to the nested dictionary under the "address" key. The new key is "zip_code" and its value is "10001". When we print my_dict, it reflects this addition, showing the updated nested dictionary with the new key-value pair included.

