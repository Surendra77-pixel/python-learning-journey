
#                        Naming a module 

#1. yoou can name the module anythiung you want but it must have a file extension .py

#2. the name of the module should be a valid Python identifier, which means it should start with a letter or an underscore and can only contain letters, numbers, and underscores. For example, my_module is a valid module name, but 1module is not a valid module name because it starts with a number.  

#3. it is a good practice to use lowercase letters and underscores to separate words in the module name. For example, my_module is a good module name, but MyModule is not a good module name because it uses uppercase letters.

#4. the module name should be descriptive and should reflect the purpose of the module. For example, if you are creating a module that contains functions for working with strings, you could name the module string_utils or string_helpers.

#5. it is also a good practice to avoid using reserved keywords as module names. For example, you should not name your module if, else, for, while, etc. because these are reserved keywords in Python and can cause syntax errors when you try to import the module.

#1. Importing functions from a module and renaming them using the as keyword:

#  When you import a function from a module, you can use the as keyword to give it a different name in your code. This can be useful if the original function name is long or if you want to avoid naming conflicts with other functions in your code. For example, if you want to import the sqrt() function from the math module and rename it to square_root, you would write from math import sqrt as square_root. Here is an example:

#creating a module named my_module.py

def greeting(name):
    print("hello, " + name + "!")

#main.py

from my_module import greeting as greet
greet("surendra")   

#Output- hello, surendra! - In this example, we have a module named my_module that contains a function called greeting. In the main.py file, we import the greeting function from my_module and rename it to greet using the as keyword. We then call the greet function with the argument "surendra", which prints "hello, surendra!" to the console. This demonstrates how you can import a function from a module and give it a different name in your code using the as keyword.


