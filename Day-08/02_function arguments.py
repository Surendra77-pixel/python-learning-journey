
#1.Arguments in function -----

#Arguments are the values that you pass to a function when you call it. They are used to provide input to the function so that it can perform its task. In Python, you can define a function with parameters, which are placeholders for the arguments that will be passed when the function is called.

#example: 

def my_function(fname):
    print(fname+"refsnes")
my_function("emil ")
my_function("Tobias ")
my_function("Linus ") #output: emil refsnes, Tobias refsnes, Linus refsnes
#In this example, the my_function takes one parameter called fname. When we call the function with different arguments ("emil ", "Tobias ", and "Linus "), it prints a message that combines the argument with the string "refsnes". Each time we call the function, it uses the provided argument to generate a different output.

#T2.he parameter vs argument:

#In the example above, fname is a parameter of the my_function, while "emil ", "Tobias ", and "Linus " are arguments that we pass to the function when we call it. Parameters are defined in the function definition and act as placeholders for the values that will be provided when the function is called, while arguments are the actual values that you pass to the function to be used in its execution.


#3.number of arguments:

#A function can have any number of parameters, and you can pass the corresponding number of arguments when calling the function. For example:
def my_functions(fname, lname):
    print(fname + " " + lname)
my_functions("John", "Doee") #output: John Doe
#In this example, the my_function takes two parameters, fname and lname. When we call the function with the arguments "John" and "Doe", it prints the full name "John Doe". You can define a function with as many parameters as needed, and you must provide the corresponding number of arguments when calling the function to avoid errors. If you don't provide the correct number of arguments, it will raise a TypeError. For example:
def my_functions_error(fname, lname):
    print(fname + " " + lname)
my_functions_error("John", "Doe") #This will print: John Doe

#4.default parameters- 

#If the function is called without an argument, it uses the default values

def my_function(name="surendra"):
    print("hello",name)
my_function("prem")
my_function("emil")
my_function("kiran")
my_function() #output: hello prem, hello emil, hello kiran, hello surendra
#In this example, the my_function has a default parameter name with the value "surendra". When we call the function with specific arguments ("prem", "emil", and "kiran"), it prints a greeting with those names. However, when we call the function without providing an argument, it uses the default value "surendra" and prints "hello surendra". This allows us to call the function without arguments while still having a meaningful output. 


#5.keyword arguments-

#When you call a function, you can specify the arguments using the parameter names, which allows you to pass the arguments in any order. This is known as keyword arguments. For example:
def my_functions(name, age):
    print(f"Name: {name}, Age: {age}")
my_functions(age=30, name="Alice") #output: Name: Alice, Age: 30
#In this example, the my_functions takes two parameters, name and age. When we call the function, we use keyword arguments by specifying the parameter names (age and name) along with their corresponding values (30 and "Alice"). This allows us to pass the arguments in any order, and the function will correctly associate the values with the respective parameters, resulting in the output "Name: Alice, Age: 30".


#6.positional arguments-    

#When you call a function, you can pass the arguments in the same order as the parameters are defined in the function. This is known as positional arguments.
# The order mostly matters in the positional arguments because the function will assign the values to the parameters based on their position. For example:
def my_function(name, age):
    print(f"Name: {name}, Age: {age}")  
# no need to add the keywords For example:
def my_function(name, age):
    print(f"Name: {name}, Age: {age}")
my_function("Alice", 30) #output: Name: Alice, Age: 30
#In this example, the my_function takes two parameters, name and age. When we call the function, we pass the arguments "Alice" and 30 in the same order as the parameters are defined. This is known as positional arguments, and it allows us to call the function without specifying the parameter names, as long as we provide the arguments in the correct order. The output will be "Name: Alice, Age: 30".


#7.variable-length arguments-

#Sometimes, you may want to define a function that can accept a variable number of arguments. In Python, you can use *args to allow a function to accept any number of positional arguments, and **kwargs to allow a function to accept any number of keyword arguments. For example:
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
my_function(1, 2, 3, name="Alice", age=30)
#output: Positional arguments: (1, 2, 3), Keyword arguments:
#In this example, the my_function is defined to accept variable-length arguments using *args for positional arguments and **kwargs for keyword arguments. When we call the function with a mix of positional and keyword arguments, it prints the positional arguments as a tuple (1, 2, 3) and the keyword arguments as a dictionary {'name': 'Alice', 'age': 30}. This allows us to create flexible functions that can handle different numbers of arguments without needing to define them explicitly in the function signature.


#mixing positional and keyword arguments-

#You can mix positional and keyword arguments when calling a function. However, positional arguments must come before keyword arguments. For example:
def my_function(name, age):
    print("i have a friend named", name, "who is", age, "years old.")
my_function("Alice", age=30)
#output: i have a friend named Alice who is 30 years old.






