
#Getting the dic values as list

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
values_list = list(my_dict.values())    
print(values_list) #output: ['Alice', 30, 'New York'] - The values() method returns a view of all the values in the dictionary, and the list() function converts this view to a list. When we print values_list, it shows a list of all the values present in the dictionary my_dict.   

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(list(my_dict.values())) #output: ['Alice', 30, 'New York'] - The dict() function is used to create a new dictionary from my_dict, and then the list() function is applied to this new dictionary to get a list of its values. When we print this list, it shows all the values present in the original dictionary my_dict.


# We can also use a list comprehension to get the values of a dictionary as a list. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
values_list = [value for value in my_dict.values()]
print(values_list) #output: ['Alice', 30, 'New York'] - The list comprehension iterates over the values of the dictionary my_dict using the values() method and creates a new list called values_list that contains all the values from the dictionary. When we print values_list, it shows a list of all the values present in the dictionary my_dict.

