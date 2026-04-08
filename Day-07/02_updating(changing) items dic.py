
#1.we can change the items in a dictionary by using the key name. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
my_dict["age"] = 31
print(my_dict) #output: {'name': 'Alice', 'age': 31, 'city': 'New York'} - The value associated with the key "age" in the dictionary my_dict is updated from 30 to 31. When we print the dictionary, it reflects this change, showing the updated value for the "age" key while the other key:value pairs remain unchanged.

#2.update() method -

#  we can also use the update() method to change the items in a dictionary. The update() method takes a dictionary as an argument and updates the key:value pairs in the original dictionary with the key:value pairs from the provided dictionary. Here is an example:

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
my_dict.update({"age": 31, "city": "Los Angeles"})
print(my_dict) #output: {'name': 'Alice', 'age': 31, 'city': 'Los Angeles'} - The update() method is called on the dictionary my_dict with another dictionary as an argument that contains the key:value pairs to be updated. In this case, the "age" key is updated from 30 to 31, and the "city" key is updated from "New York" to "Los Angeles". When we print the dictionary, it reflects these changes, showing the updated values for both keys while the "name" key remains unchanged.



