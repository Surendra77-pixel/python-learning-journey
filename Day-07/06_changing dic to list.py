
#Changing a Dictionary to a List

# We can convert the keys, values, or items of a dictionary to a list using the list() function. Here are some examples:

# 1. Converting Keys to a List
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
keys_list = list(my_dict.keys())
print(keys_list) #output: ['name', 'age', 'city'] - The keys() method returns a view of all the keys in the dictionary, and the list() function converts this view to a list.

# 2. Converting Values to a List
values_list = list(my_dict.values())
print(values_list) #output: ['Alice', 30, 'New York'] - The values() method returns a view of all the values in the dictionary, and the list() function converts this view to a list.

# 3. Converting Items to a List
items_list = list(my_dict.items())
print(items_list) #output: [('name', 'Alice'), ('age', 30), ('city', 'New York')] - The items() method returns a view of all the key-value pairs in the dictionary, and the list() function converts this view to a list.


