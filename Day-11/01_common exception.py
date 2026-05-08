
#               Common Exception Handling

#The exception is an error that happens while the program is running and it can be handled using try-except blocks.

##There are different types of exceptions in Python, and some of the common ones include:


#1.syntax error:

#  This occurs when there is a mistake in the syntax of the code. For example, missing a colon at the end of a function definition.here is an example of a syntax error:
def my_function():
    print("Hello, World!)
#In this example, we forgot to add a colon at the end of the function definition, which will result in a syntax error when we try to run the code. To fix this error, we need to add a colon at the end of the function definition like this:
def my_function():
    print("Hello, World!")


#2.name error: 

# This occurs when you try to use a variable or function that has not been defined. For example:
print(x)
#In this example, we are trying to print the value of a variable x that has not been defined, which will result in a name error. To fix this error, we need to define the variable x before using it like this:
x = 10
print(x)


#3.type error:

# This occurs when you try to perform an operation on a value of the wrong type. For example:
a = "10"
b = 5
print(a + b) #output: TypeError: can only concatenate str (not "int") to str
#In this example, we are trying to add a string and an integer, which will result in a type error. To fix this error, we need to convert the string to an integer before performing the addition like this:
a = "10"
b = 5
print(int(a) + b) #output: 15


#4.value error:

# This occurs when you try to convert a value to a type that is not compatible. For example:
a = "abc"
b = int(a) #output: ValueError: invalid literal for int() with base 10: 'abc'
#In this example, we are trying to convert a string that cannot be converted to an integer, which will result in a value error. To fix this error, we need to make sure that the string can be converted to an integer before trying to convert it like this:
a = "123"
b = int(a) #output: 123


#5.index error:

# This occurs when you try to access an index that is out of range. For example:
my_list = [1, 2, 3]
print(my_list[3]) #output: IndexError: list index out of range
#In this example, we are trying to access the index 3 of a list that only has 3 elements (index 0, 1, and 2), which will result in an index error. To fix this error, we need to make sure that we are accessing a valid index like this:
my_list = [1, 2, 3]
print(my_list[2]) #output: 3


#6.key error:

# This occurs when you try to access a key that does not exist in a dictionary. For example:
my_dict = {"name": "Alice", "age": 30}
print(my_dict["gender"]) #output: KeyError: 'gender'
#In this example, we are trying to access the key "gender" in a dictionary that only has the keys "name" and "age", which will result in a key error. To fix this error, we need to make sure that we are accessing a valid key like this:
my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"]) #output: Alice


#7.attribute error:

# This occurs when you try to access an attribute that does not exist for an object. For example:
my_list = [1, 2, 3]
print(my_list.length) #output: AttributeError: 'list' object has no attribute 'length'
#In this example, we are trying to access the attribute "length" of a list object, which does not exist, resulting in an attribute error. To fix this error, we need to use the correct method to get the length of the list like this:
my_list = [1, 2, 3]
print(len(my_list)) #output: 3


#8.zero division error:

# This occurs when you try to divide a number by zero. For example:
a = 10  
b = 0
print(a / b) #output: ZeroDivisionError: division by zero
#In this example, we are trying to divide a number by zero, which is not allowed in mathematics. When we run this code, Python raises a ZeroDivisionError exception because it cannot perform the division operation. To fix this error, we need to make sure that we are not dividing by zero like this:
a = 10
b = 2
print(a / b) #output: 5.0


#9.file not found error:

# This occurs when you try to open a file that does not exist. For example:
file = open("non_existent_file.txt", "r") #output: FileNotFound
Error: [Errno 2] No such file or directory: 'non_existent_file.txt'
#In this example, we are trying to open a file that does not exist, which will result in a file not found error. To fix this error, we need to make sure that the file we are trying to open exists and is in the correct location like this:
file = open("existing_file.txt", "r") #output: file object at 0x7f8c8c8c8c8c>


#10.import error:

# This occurs when you try to import a module that does not exist. For example:
import non_existent_module #output: ModuleNotFoundError: No module named 'non_existent_module'
#In this example, we are trying to import a module that does not exist, which will result in an import error. To fix this error, we need to make sure that the module we are trying to import exists and is installed in our Python environment like this:
import math #output: <module 'math' (built-in)>


#11.module not found error:

# This occurs when you try to import a module that is not installed in your Python environment. For example:
import non_existent_module #output: ModuleNotFoundError: No module named 'non_existent_module'
#In this example, we are trying to import a module that is not installed in our Python environment, which will result in a module not found error. To fix this error, we need to make sure that the module we are trying to import is installed in our Python environment like this:
import math #output: <module 'math' (built-in)>


#12.runtime error:

# This occurs when an error happens during the execution of the program. For example:
a = 10
b = 0
print(a / b) #output: ZeroDivisionError: division by zero
#In this example, we are trying to divide a number by zero, which is not allowed in mathematics. When we run this code, Python raises a ZeroDivisionError exception because it cannot perform the division operation. To fix this error, we need to make sure that we are not dividing by zero like this:
a = 10
b = 2
print(a / b) #output: 5.0


#13.Exception:

# This is a base class for all exceptions in Python. It can be used to catch any exception that occurs during the execution of the program. For example:
try:
    a = 10
    b = 0
    print(a / b)
except Exception as e:
    print("An error occurred:", e)
#In this example, we are trying to divide a number by zero, which will raise a ZeroDivisionError exception. However, since we are catching the exception using the base class Exception, it will catch any exception that occurs and print a message along with the error message. To fix this error, we need to make sure that we are not dividing by zero like this:
try:
    a = 10
    b = 2
    print(a / b)    
except Exception as e:
    print("An error occurred:", e)

#14.keyboard interrupt:

# This occurs when the user interrupts the program execution by pressing Ctrl+C. For example:
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted by user")
#In this example, we have an infinite loop that will keep running until the user interrupts it by pressing Ctrl+C. When the user interrupts the program, it will raise a KeyboardInterrupt exception, which we catch and print a message to inform the user that the program has been interrupted. To fix this error, we can simply run the program without interrupting it like this:
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted by user")




