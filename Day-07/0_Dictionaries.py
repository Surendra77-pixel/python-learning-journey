
#Dictionaries-

#Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and does not allow duplicates.

#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


#Creating a dictionary - We can create a dictionary using curly braces {} and separating keys and values with a colon :

#key:value pairs - A dictionary consists of key:value pairs, where each key is unique and maps to a specific value. The keys in a dictionary must be immutable (such as strings, numbers, or tuples), while the values can be of any data type (including lists, other dictionaries, etc.). Here is an example of a dictionary with key:value pairs:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict) #output: {'name': 'Alice', 'age': 30, 'city': 'New York'} - The dictionary my_dict contains three key:value pairs that store the name, age, and city of a person. When we print the dictionary, it displays the key:value pairs in an ordered manner.

#The dictionaries are used in real life to store data in a structured way. For example, we can use a dictionary to store information about a person, such as their name, age, and address. Here is an example of a dictionary that stores information about a person:
person = {
    "name": "John",
    "age": 30,
    "address": "123 Main St"
}
print(person)#ouput:{name': 'John', 'age': 30, 'address': '123 Main St'} - The dictionary person contains three key:value pairs that store the name, age, and address of the person. When we print the dictionary, it displays the key:value pairs in an ordered manner.

#the dictionary can  alos store any data type as a value, including lists, tuples, and even other dictionaries. Here is an example of a dictionary that contains a list as a value:
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(person) #output: {'first_name': 'Asabeneh', 'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland', 'is_marred': True, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'address': {'street': 'Space street', 'zipcode': '02210'}} - The dictionary person contains various key:value pairs, including a list of skills and a nested dictionary for the address. When we print the dictionary, it displays all the key:value pairs in an unordered manner.


#dictionary length - We can find the number of key:value pairs in a dictionary using the len() function. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(len(my_dict)) #output: 3 - The len() function is called with the dictionary my_dict as an argument, and it returns the number of key:value pairs in the dictionary, which is 3 in this case.

#dictinary items data types - The keys in a dictionary must be immutable data types, such as strings, numbers, or tuples. The values in a dictionary can be of any data type, including lists, other dictionaries, etc. Here is an example of a dictionary with different data types for keys and values:

my_dict = {
    "name": "Alice",  # string key and string value
    42: "The answer to the ultimate question of life, the universe, and everything",  # integer key and string value
    (1, 2): [3, 4, 5],  # tuple key and list value
    "is_student": True  # string key and boolean value
}
print(my_dict) #output: {'name': 'Alice', 'age': 30, 'city': 'New York', 42: 'The answer to the ultimate question of life, the universe, and everything', (1, 2): [3, 4, 5], 'is_student': True} - The dictionary my_dict contains various key:value pairs with different data types for keys and values. When we print the dictionary, it displays all the key:value pairs in an ordered manner.


#type of the dictionary - We can check the type of a dictionary using the type() function. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(type(my_dict)) #output: <class 'dict'> - The type() function is called with the dictionary my_dict as an argument, and it returns <class 'dict'>, indicating that my_dict is of type dictionary.


#The dict() constructor - We can also create a dictionary using the dict() constructor. The dict() constructor takes an iterable of key:value pairs as an argument and creates a dictionary from it. Here is an example:
my_dict = dict(name="Alice", age=30, city="New York")
print(my_dict) #output: {'name': 'Alice', 'age': 30, 'city': 'New York'} - The dict() constructor is called with keyword arguments to create a dictionary with the specified key:value pairs. When we print the dictionary, it displays the key:value pairs in an ordered manner.


