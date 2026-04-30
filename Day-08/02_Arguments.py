
#1.The arguments are the values that we pass to a function when we call it. They are used to provide input to the function, allowing it to perform its task based on the provided data. In Python, we can define functions that take arguments, and we can also specify default values for those arguments.

#example of a function with arguments:

def my_function(fname):
    print(fname+"student")
my_function("Alice") #output: Alicestudent

#1.2.The parameter is fname, and when we call the function my_function("Alice"), we are passing the argument "Alice" to the function. The function then uses this argument to execute its code, which results in printing "Alicestudent".

#example of parameters
def greet(name):
    print(f"Hello, {name}!")
greet("Alice") #output: Hello, Alice!


#2.The parameter vs argument:

#1. A parameter is a variable that is defined in the function definition and serves as a placeholder for the value that will be passed to the function when it is called. An argument, on the other hand, is the actual value that is passed to the function when it is called.

#2. Parameters are used in the function definition to specify what kind of input the function expects, while arguments are used when calling the function to provide the actual input values.

#3. Parameters are defined in the function signature, while arguments are provided in the function call.

def my_function(name): #name is a parameter
    print(f"Hello, {name}!")
my_function("Alice") #output: Hello, Alice! - "Alice" is an argument that is passed to the function my_function when it is called. The parameter name in the function definition is a placeholder for the value that will be provided as an argument when the function is called. In this case, the argument "Alice" is passed to the function, and it uses that value to execute its code, resulting in printing "Hello, Alice!".

#3.number of arguments:

#The no of aruguments is known as the function must be called with the correct number of arguments. If you provide too few or too many arguments, Python will raise a TypeError. For example:

def my_function(name, age):
    print(name +" "+age)
    my_function("Alice") #output: TypeError: my_function() missing 1 required positional argument: 'age' - In this example, the function my_function is defined to take two parameters, name and age. When we call the function with only one argument ("Alice"), it raises a TypeError because the function expects two arguments but only one was provided. To fix this error, we need to provide both arguments when calling the function, like this: my_function("Alice", 30).

def my_function(name, age):
    print(name +" "+age)
my_function("Alice", 30) #output: Alice 30 - In this example, we call the function my_function with two arguments, "Alice" and 30. The function takes these arguments and executes its code, which results in printing "Alice 30". This is the correct way to call the function since it matches the number of parameters defined in the function signature.



#4.Default arguments:

#Default arguments are values that are assigned to parameters in a function definition. If the caller does not provide a value for that parameter when calling the function, the default value will be used. This allows you to call the function with fewer arguments than the number of parameters defined in the function. For example:

def my_function(name="surendra"):
    print("hello"," ",name)
my_function("kiran")
my_function("abhi")
my_function("gowtham")
my_function()#output: hello kiran
#hello abhi
#hello gowtham
#hello surendra - In this example, the function my_function is defined with a default argument name that has a default value of "surendra". When we call the function with an argument (like "kiran", "abhi", or "gowtham"), it uses the provided argument to execute its code. However, when we call the function without any arguments (my_function()), it uses the default value "surendra" for the parameter name, resulting in printing "hello surendra". This demonstrates how default arguments work in Python functions.


#5.keyword arguments:

#Keyword arguments are a way to specify arguments in a function call by explicitly naming them. This allows you to provide arguments in any order, as long as you specify the parameter names. For example:
def my_function(name, age):
    print(f"Name: {name}, Age: {age}")
my_function(age=30, name="Alice") #output: Name: Alice, Age: 30 - In this example, we call the function my_function using keyword arguments. We specify the parameter names (age and name) along with their corresponding values (30 and "Alice"). This allows us to provide the arguments in any order, and the function will correctly associate the values with the respective parameters. As a result, it prints "Name: Alice, Age: 30".\

#In the keyword aruguments the order dosent matters 

#6.positional arguments:

#when you call a function with the arguments without using keywords , they are called positional arguments. The order of the arguments matters in this case, as they are assigned to the parameters based on their position in the function call. For example:
def my_function(name, age):
    print(f"Name: {name}, Age: {age}")
my_function("Alice", 30) #output: Name: Alice, Age: 30 - In this example, we call the function my_function with positional arguments. The first argument "Alice" is assigned to the parameter name, and the second argument 30 is assigned to the parameter age based on their position in the function call. As a result, it prints "Name: Alice, Age: 30". In this case, the order of the arguments matters because they are assigned to the parameters based on their position. If we were to switch the order of the arguments (my_function(30, "Alice")), it would lead to incorrect output since 30 would be assigned to name and "Alice" would be assigned to age.

#switching the order of the arguments
def my_function(name, age):
    print(f"Name: {name}, Age: {age}")
my_function(30, "Alice") #output: Name: 30, Age: Alice - In this example, we call the function my_function with positional arguments, but we switch the order of the arguments. The first argument 30 is assigned to the parameter name, and the second argument "Alice" is assigned to the parameter age based on their position in the function call. As a result, it prints "Name: 30, Age: Alice", which is incorrect because 30 should be the age and "Alice" should be the name. This demonstrates how the order of positional arguments matters when calling a function.

#7.mixing positional and keyword arguments:

#You can mix positional and keyword arguments in a function call, but there are some rules to follow. Positional arguments must come before keyword arguments in the function call. For example:

def my_function(animal , name , age):
    print(f"Animal: {animal}, Name: {name}, Age: {age}")
my_function("Dog", name="Buddy", age=5) #output: Animal: Dog, Name: Buddy, Age: 5 - In this example, we call the function my_function with a mix of positional and keyword arguments. The first argument "Dog" is a positional argument that is assigned to the parameter animal. The next two arguments are keyword arguments (name="Buddy" and age=5) that are assigned to the parameters name and age, respectively. This is valid because the positional argument comes before the keyword arguments in the function call. As a result, it prints "Animal: Dog, Name: Buddy, Age: 5".

#invalid mixing of positional and keyword arguments
def my_function(animal , name , age):
    print(f"Animal: {animal}, Name: {name}, Age: {age}")
my_function(name="Buddy", age=5, "Dog") #output: SyntaxError: positional argument follows keyword argument - In this example, we attempt to call the function my_function with a mix of keyword and positional arguments, but we place the positional argument "Dog" after the keyword arguments. This is invalid syntax in Python because positional arguments must come before keyword arguments in a function call. As a result, it raises a SyntaxError indicating that a positional argument follows a keyword argument. To fix this error, we need to ensure that all positional arguments are placed before any keyword arguments in the function call.  

