
#accesing the items of the dictionary -

# we can access the items of a dictionary using the keys. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict["name"]) #output: Alice - The value associated with the key "name" in the dictionary my_dict is accessed using square brackets, and it returns "Alice".


#if the other key we accces which is not present in the dictionary it will give an error. For example:

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
x=my_dict["country"]
print(x)
print(my_dict["country"])
 
 # This will raise a KeyError because the key "country"  is not present in the dictionary -----to avoid this error we can use the get() method to access the value of a key in a dictionary. The get() method returns None if the key is not found in the dictionary, instead of raising an error. Here is an example:


#2.get() method -

#The get method is used to access the value of a key in a dictionary. It takes the key as an argument and returns the corresponding value. If the key is not found in the dictionary, it returns None (or a specified default value). Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict.get("name")) #output: Alice - The get() method is called with the key "name" as an argument, and it returns the value "Alice" associated with that key in the dictionary my_dict.
print(my_dict.get("country")) #output: None - The get() method is called with the key "country" as an argument, and since "country" is not present in the dictionary my_dict, it returns None instead of raising a KeyError.
print(my_dict.get("country", "Not Found")) #output: Not Found - The get() method is called with the key "country" and a default value "Not Found" as arguments. Since "country" is not present in the dictionary my_dict, it returns the specified default value "Not Found" instead of None or raising a KeyError.


#3. keys() method -

# The keys() method returns a view object that displays a list of all the keys in the dictionary. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict.keys()) #output: dict_keys(['name', 'age', 'city']) - The keys() method is called on the dictionary my_dict, and it returns a view object that contains all the keys in the dictionary. When printed, it shows the keys as a list-like object.

#one small example --

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x)

car["color"] = "white"

print(x) 
#output: dict_keys(['brand', 'model', 'year']) - The keys() method is called on the dictionary car, and it returns a view object that contains all the keys in the dictionary. When printed, it shows the keys as a list-like object.
#output: dict_keys(['brand', 'model', 'year', 'color']) - After adding a new key "color" to the dictionary car, the view object x that was created using the keys() method reflects this change. When we print x again, it now includes the new key "color" along with the existing keys, demonstrating that the view object is dynamic and updates to reflect changes in the dictionary.


#4.values() method -

# The values() method returns a view object that displays a list of all the values in the dictionary. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict.values()) #output: dict_values(['Alice', 30, 'New York']) - The values() method is called on the dictionary my_dict, and it returns a view object that contains all the values in the dictionary. When printed, it shows the values as a list-like object.

#one small example --

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)
car["color"] = "white"
print(x)
#output: dict_values(['Ford', 'Mustang', 1964]) - The values() method is called on the dictionary car, and it returns a view object that contains all the values in the dictionary. When printed, it shows the values as a list-like object.
#output: dict_values(['Ford', 'Mustang', 1964, 'white']) - After adding a new key "color" with the value "white" to the dictionary car, the view object x that was created using the values() method reflects this change. When we print x again, it now includes the new value "white" along with the existing values, demonstrating that the view object is dynamic and updates to reflect changes in the dictionary. 


#5.items() method -

# The items() method returns a view object that displays a list of all the key:value pairs in the dictionary as tuples. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict.items()) #output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')]) - The items() method is called on the dictionary my_dict, and it returns a view object that contains all the key:value pairs in the dictionary as tuples. When printed, it shows the key:value pairs as a list of tuples.


#one small example --

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
car["color"] = "white"
print(x)
#output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]) - The items() method is called on the dictionary car, and it returns a view object that contains all the key:value pairs in the dictionary as tuples. When printed, it shows the key:value pairs as a list of tuples.
#output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'white')]) - After adding a new key "color" with the value "white" to the dictionary car, the view object x that was created using the items() method reflects this change. When we print x again, it now includes the new key:value pair ('color', 'white') along with the existing key:value pairs, demonstrating that the view object is dynamic and updates to reflect changes in the dictionary.



#using if statement to access the items of the dictionary -
# we can also use an if statement to check if a key exists in the dictionary before accessing its value. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}   
if "name" in my_dict:
    print(my_dict["name"]) #output: Alice - The if statement checks if the key "name" exists in the dictionary my_dict using the in keyword. Since it does exist, the code inside the if block is executed, and it prints the value associated with the key "name", which is "Alice".