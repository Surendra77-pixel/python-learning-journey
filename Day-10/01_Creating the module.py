
# creating the module-

#1.To create a module just save the code you want in a file with the file extension .py for example, if you want to create a module named my_module, you would create a file named my_module.py and write your code in that file

#should be saved as my_module.py
 
def greeting(name):
    print("hello, " + name + "!")


#2.To use the module in another Python file, you can import it using the import statement. For example, if you want to use the greeting() function from the my_module, you would write import my_module at the top of your Python file and then call the function using my_module.greeting("your name").here is the example-

import my_module
my_module.greeting("surendra")
#Output- hello, surendra!

#note- when you import a module, Python looks for the module in the current working directory and in the directories listed in the PYTHONPATH environment variable. If the module is not found, it raises a ModuleNotFoundError. and  When using a function from a module, use the syntax: module_name.function_name.
