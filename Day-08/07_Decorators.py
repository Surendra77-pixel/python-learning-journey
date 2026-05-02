
#Decorators -

#A decorator is a design pattern in Python that allows you to modify the behavior of a function or a class method without changing its source code. It is a higher-order function that takes another function as an argument and returns a new function that can be used in place of the original function. Decorators are often used to add functionality to existing functions, such as logging, timing, or authentication, without modifying the original code.

#Example of a simple decorator -

def my_decorator(func):
    def myinner():
        return func().upper()
    return myinner
@change_case
def my_function():
    return "hello, world!"
print(my_function())  # Output: "HELLO, WORLD!" - In this example, we define a decorator function called my_decorator that takes a function func as an argument. Inside the decorator, we define an inner function myinner that calls the original function func and converts its result to uppercase using the upper() method. The decorator then returns the inner function myinner. We use the @change_case syntax to apply the decorator to the my_function, which means that when we call my_function(), it will actually call the decorated version of the function that converts the output to uppercase. As a result, when we print the result of calling my_function(), it outputs "HELLO, WORLD!" instead of "hello, world!". This demonstrates how decorators can be used to modify the behavior of a function without changing its source code.

#Multiple decorators calls-

#A decorator is a design pattern in Python that allows you to modify the behavior of a function or a class method without changing its source code. When multiple decorators are applied to a function, they are executed in a specific order. The decorators are applied from the innermost to the outermost, meaning that the decorator closest to the function definition is executed first, and then the next decorator is executed on the result of the previous one, and so on. This allows you to stack multiple decorators on top of each other to create complex behavior modifications for your functions. Each decorator can add its own functionality or modify the behavior of the function in a specific way, and they will be executed in the order they are defined.example of multiple decorators calls-

def change_case(func):
    def myinner():
        return func().upper()
    return myinner
@change_case
def my_function():
    return "hello, world!"
@change_case
def another_function():
    return "python is great!"   
print(my_function())  # Output: "HELLO, WORLD!"
print(another_function())  # Output: "PYTHON IS GREAT!" - In this example, we have two functions, my_function and another_function, both decorated with the change_case decorator. The change_case decorator takes a function as an argument and returns a new function that converts the output of the original function to uppercase. When we call my_function(), it executes the decorated version of the function, which converts the output to uppercase, resulting in "HELLO, WORLD!". Similarly, when we call another_function(), it also executes the decorated version of the function, converting its output to uppercase and resulting in "PYTHON IS GREAT!". This demonstrates how multiple decorators can be applied to different functions to modify their behavior in a consistent way.

