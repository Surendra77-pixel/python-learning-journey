
#                   *args and **kwargs in Python

#In Python, *args and **kwargs are used to allow a function to accept an arbitrary number of arguments.

#1. *args allows a function to accept any number of positional arguments. The arguments are passed as a tuple to the function. For example:
def my_function(*args):
    for arg in args:
        print(arg)
my_function("surendra", "20", "python", "programming")
#output: surendra
#         20
#         python
#         programming

#2. **kwargs allows a function to accept any number of keyword arguments. The arguments are passed as a dictionary to the function. For example:
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function(name="surendra", age="20", language="python")
#output: name: surendra
#         age: 20


#3. You can also use both *args and **kwargs in the same function definition. For example:
def my_function(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function("surendra", "20", language="python", framework="django")
#output: Positional arguments:
#         surendra
#         20
#         Keyword arguments:
#         language: python
#         framework: django

#4. The *args and **kwargs can also be used to unpack arguments when calling a function. For example:

def greet(name, location):
    print("Hi there", name, "how is the weather in", location)
greet(name="Alice", location="New York")
# Output: Hi there Alice how is the weather in New York
my_dict = {"name": "Alice", "location": "New York"}
greet(**my_dict)
# The ** operator unpacks the dictionary, passing its key-value pairs as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York

