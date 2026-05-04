
#1.Breakpoint in function-

# The breakpoint() function is a built-in function in Python that allows you to set a breakpoint in your code. When the breakpoint is reached during execution, the program will pause and enter an interactive debugging session, allowing you to inspect variables, evaluate expressions, and step through the code line by line.

x=10
breakpoint()
y=20
print(x)
print(y)
#output: 10, 20 - In this example, we have a variable x with the value 10. When we call breakpoint(), it will pause the execution of the program and allow us to inspect the current state of the program. We can use the interactive debugger to check the value of x and other variables at this point in the code. After inspecting the variables, we can continue the execution of the program, which will then print the value of x, which is 10.


#2.compile() function-

# The compile() function is a built-in function in Python that compiles a source code string into a code object that can be executed by the Python interpreter. It takes three arguments: the source code as a string, the filename (which can be set to '<string>' if the source code is not from a file), and the mode (which can be 'exec' for executing statements, 'eval' for evaluating expressions, or 'single' for executing a single interactive statement).
source_code = "print('Hello, World!')"
code_object = compile(source_code, '<string>', 'exec')
exec(code_object)  # Output: Hello, World! - In this example, we define a source code string that contains a simple print statement. We then use the compile() function to compile this source code into a code object. Finally, we use the exec() function to execute the compiled code object, which results in printing "Hello, World!" to the console. This demonstrates how the compile() function can be used to dynamically compile and execute Python code from a string.


#3.exec() function- 

# The exec() function is a built-in function in Python that executes the dynamically created program, which can be a string or object code. It takes a single argument, which is the code to be executed. The code can be a string containing Python statements or an object code that has been compiled using the compile() function.
code_string = "x = 5\ny = 10\nprint(x + y)"
exec(code_string)  # Output: 15 - In this example, we define a string code_string that contains multiple lines of Python code. The code assigns the value 5 to variable x, the value 10 to variable y, and then prints the sum of x and y. When we call exec(code_string), it executes the code contained in the string, resulting in printing 15 (the sum of 5 and 10) to the console. This demonstrates how the exec() function can be used to execute dynamically created Python code from a string.


#4.eval() function-

# The eval() function is a built-in function in Python that evaluates a given expression and returns the result. It takes a single argument, which is the expression to be evaluated. The expression can be a string containing a Python expression or an object code that has been compiled using the compile() function.
expression = "2 + 3 * 4"
result = eval(expression)
print(result)  # Output: 14 - In this example, we define a string expression that contains a simple mathematical expression. We then use the eval() function to evaluate this expression, which follows the order of operations (multiplication before addition). The result of evaluating the expression is 14 (2 + (3 * 4) = 2 + 12 = 14), which is printed to the console. This demonstrates how the eval() function can be used to evaluate dynamically created Python expressions from a string.


#5.vars function-

# The vars() function is a built-in function in Python that returns the __dict__ attribute of an object, which is a dictionary containing the object's attributes and their corresponding values. It can be used to inspect the attributes of an object or to get a dictionary representation of an object's attributes.
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
my_object = MyClass("Alice", 30)
attributes = vars(my_object)
print(attributes)  # Output: {'name': 'Alice', 'age': 30} - In this example, we define a class MyClass with an __init__ method that initializes the attributes name and age. We create an instance of MyClass called my_object with the name "Alice" and age 30. When we call vars(my_object), it returns a dictionary containing the attributes of my_object and their corresponding values, which is {'name': 'Alice', 'age': 30}. This demonstrates how the vars() function can be used to inspect the attributes of an object in Python.


#6.globals() function-

# The globals() function is a built-in function in Python that returns a dictionary representing the current global symbol table. This dictionary contains all the global variables and their corresponding values that are defined in the current module or script. It can be used to access and modify global variables from within a function or to inspect the global namespace.
x = 10
print(globals()["x"])# Output: 10 - In this example, we define a global variable x with the value 10. When we call globals(), it returns a dictionary representing the global symbol table, which includes the variable x and its value. By accessing globals()["x"], we can retrieve the value of the global variable x, which is 10. This demonstrates how the globals() function can be used to access global variables from within a function or to inspect the global namespace in Python.

#7.locals() function-

# The locals() function is a built-in function in Python that returns a dictionary representing the current local symbol table. This dictionary contains all the local variables and their corresponding values that are defined in the current scope (such as within a function). It can be used to access and modify local variables from within a function or to inspect the local namespace.
def my_function():
    x = 5
    y = 10
    local_variables = locals()
    print(local_variables)  # Output: {'x': 5, 'y': 10} - In this example, we define a function my_function that initializes two local variables x and y with the values 5 and 10, respectively. When we call locals() within the function, it returns a dictionary representing the local symbol table, which includes the variables x and y along with their corresponding values. The output is {'x': 5, 'y': 10}, demonstrating how the locals() function can be used to access local variables from within a function or to inspect the local namespace in Python.


#8.Dir() function-

# The dir() function is a built-in function in Python that returns a list of the attributes and methods of an object. It can be used to inspect the properties of an object or to get a list of available methods for a particular type of object.

my_list = [1, 2, 3]
print(dir(my_list))  # Output: ['__add__', '__class__', '__contains__', ..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] - In this example, we create a list called my_list with the values [1, 2, 3]. When we call dir(my_list), it returns a list of all the attributes and methods that are available for the list object. This includes special methods (those that start and end with double underscores) as well as regular methods like append, clear, copy, count, extend, index, insert, pop, remove, reverse, and sort. This demonstrates how the dir() function can be used to inspect the properties of an object or to get a list of available methods for a particular type of object in Python.

#9.Help() function-

# The help() function is a built-in function in Python that provides a way to access the documentation of modules, classes, functions, and other objects. It can be used to get information about how to use a particular object, its methods, and its attributes.
help(list)  # Output: Help on class list in module builtins: ... - In this example, we call the help() function with the list class as an argument. This will display the documentation for the list class, including its methods and attributes. The output will provide information on how to use the list class and its various functionalities. This demonstrates how the help() function can be used to access documentation for modules, classes, functions, and other objects in Python.you can use the str(), int(), float() functions to get the documentation for those specific types as well. For example, help(str) will provide documentation for the string type, and help(int) will provide documentation for the integer type. This allows you to easily access information about how to use different types and their associated methods in Python.


#10.Collable() function-

# The callable() function is a built-in function in Python that checks if an object appears to be callable (i.e., if it can be called as a function). It returns True if the object is callable and False otherwise. This can be useful for checking if an object is a function, method, or any other type of callable object before attempting to call it.
def my_function():
    print("Hello, World!")
print(callable(my_function))  # Output: True - In this example, we define a function called my_function that prints "Hello, World!" when called. When we use the callable() function to check if my_function is callable, it returns True because my_function is indeed a function and can be called. This demonstrates how the callable() function can be used to check if an object is callable in Python.    

print(callable(print)))
print(callable(10))# Output: True, False - In this example, we check if the built-in print function is callable using callable(print), which returns True because print is a function that can be called. We also check if the integer 10 is callable using callable(10), which returns False because 10 is not a function or any other type of callable object. This further demonstrates how the callable() function can be used to check if different types of objects are callable in Python.
    