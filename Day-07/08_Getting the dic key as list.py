
#getting the dictionary key as list

# We can get the keys of a dictionary as a list by using the keys() method and converting it to a list. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}   
keys_list = list(my_dict.keys())
print(keys_list) #output: ['name', 'age', 'city'] - The keys() method returns a view of all the keys in the dictionary, and the list() function converts this view to a list. When we print keys_list, it shows a list of all the keys present in the dictionary my_dict.   


my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}   
print(list(dict(my_dict))) #output: ['name', 'age', 'city'] - The dict() function is used to create a new dictionary from my_dict, and then the list() function is applied to this new dictionary to get a list of its keys. When we print this list, it shows all the keys present in the original dictionary my_dict.

