
#                         Modulus 


#A module is simply a file that contains Python code (functions, variables, classes) that you can reuse in another program.

#What is the module - 

#A module is a file containg code ( functions, variables, classes) that you can reuse in another program.for example, if you have a file named my_module.py that contains some functions and variables, you can import that module into another Python file and use its functions and variables without having to rewrite the code. This promotes code reusability and helps to organize your code into logical sections.

#Where the module is stored-

#When you import a module in Python, the interpreter looks for the module in a specific order. It first checks if the module is built-in, then it looks for the module in the current working directory, and finally it searches for the module in the directories listed in the PYTHONPATH environment variable. If the module is not found in any of these locations, a ModuleNotFoundError is raised.

#Where the module are used 

#1.math caluculation
#2. file handling
#3. web development
#4. data analysis

#When using a function from a module , use this syntax- module_name.function_name() for example, if you want to use the sqrt() function from the math module, you would write math.sqrt().here is the example-

import math
result = math.sqrt(16)
print(result) #Output- 4.0


#In the python there are two types of modules-

#1. Built-in modules- These are the modules that come pre-installed with Python. They provide a wide range of functionality and can be used without any additional installation. Examples of built-in modules include math, datetime, os, sys, random, and many more.

#2. User-defined modules- These are the modules that you create yourself. You can write your own functions, variables, and classes in a Python file and then import that file as a module in another Python file. This allows you to organize your code and reuse it across different projects.

