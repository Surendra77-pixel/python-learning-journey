
#                   variables in module

#1. A variable in a module is a name that refers to a value or an object defined within the module. It can be used to store data, functions, classes, or any other type of object that is defined in the module. Variables in a module can be accessed and modified by other parts of the program that import the module.

#The module can contain functions as already described , but also varibales of all the types like int, float, string, list, tuple, dictionary etc. For example, if we have a module named my_module.py that contains a variable named my_variable, we can import that module into another Python file and access the value of my_variable using the syntax my_module.my_variable. Here is an example:

#------> my_module.py

my_variable = "Hello, World!"

# main.py
import my_module
print(my_module.my_variable) #Output- Hello, World!

#------> moduledic.py

person={
    "name": "surendra",
    "age": 25,
    "city": "delhi"
}

#out.py

import moduledic
a=moduledic.person["age"]
print(a) #Output- 25



