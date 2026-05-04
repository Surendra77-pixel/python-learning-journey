

#scope 

#In Python, scope refers to the region of a program where a particular variable or name is accessible. There are four types of scopes in Python: local, enclosing, global, and built-in.

#1. Local Scope:

#  A variable defined inside a function is said to have a local scope. It can only be accessed within that function and is not visible outside of it.

from ast import In


def my_function():
    x = 10  # x is a local variable
    print(x)  # Output: 10


#2. Enclosing Scope:

#  This scope refers to the variables defined in the enclosing function. If a variable is not found in the local scope, Python looks for it in the enclosing scope.

def outer_function():
    x = 20  # x is in the enclosing scope

    def inner_function():
        print(x)  # Output: 20

    inner_function()


#3. Global Scope:

#  A variable defined at the top level of a module or script is said to have a global scope. It can be accessed from anywhere in the program.
y = 30  # y is a global variable

def another_function():
    print(y)  # Output: 30
another_function()

#4. Built-in Scope:

#  This scope contains the names of built-in functions and exceptions that are always available in Python. These names can be accessed from any part of the program without needing to import any modules.
print(len("Hello"))  # Output: 5 - In this example, the len() function is a built-in function that is available in the built-in scope. We can call it directly without needing to define it ourselves or import any modules. The len() function takes a string as an argument and returns the number of characters in that string, which is 5 in this case. This demonstrates how built-in functions are accessible from any part of the program due to their presence in the built-in scope.

#5. Function inside Function:

def my_func():
    x=300
    def myinnerfunc():
        print(x)
        myinnerfunc()
my_func() #output: 300 - In this example, we have a function my_func that defines a local variable x with the value 300. Inside my_func, there is another function called myinnerfunc that prints the value of x. When we call my_func(), it executes the code inside it, which includes calling myinnerfunc(). Since myinnerfunc() has access to the variables in its enclosing scope (my_func), it can access and print the value of x, which is 300. This demonstrates how functions defined inside other functions can access variables from their enclosing scope.

#6.naming variables-

#if you define a variable with the same name in different scopes, the variable in the innermost scope will take precedence over the variables in the outer scopes. This is known as variable shadowing. For example:

x = 100  # global variable
def my_func():
    x = 200  # local variable that shadows the global variable
    print(x)  # Output: 200
my_func()
print(x)  # Output: 100 - In this example, we have a global variable x with the value 100. Inside the function my_func, we define a local variable x with the value 200, which shadows the global variable. When we call my_func(), it prints the value of the local variable x, which is 200. However, when we print x outside of the function, it refers to the global variable, which still has the value 100. This demonstrates how variable shadowing works in Python, where the innermost variable takes precedence over variables in outer scopes.

#7. The global keyword:

#  If you want to modify a global variable inside a function, you can use the global keyword to indicate that you are referring to the global variable rather than creating a new local variable. For example:
x = 100  # global variable
def my_func():
    global x  # indicate that we want to use the global variable x
    x = 200  # modify the global variable
    print(x)  # Output: 200
my_func()
print(x)  # Output: 200 - In this example, we have a global variable x with the value 100. Inside the function my_func, we use the global keyword to indicate that we want to refer to the global variable x instead of creating a new local variable. We then modify the value of x to 200. When we call my_func(), it prints the modified value of x, which is 200. After calling my_func(), when we print x outside of the function, it also reflects the modified value of 200, demonstrating that we successfully modified the global variable using the global keyword.

#8.The nonlocal keyword:

#  If you want to modify a variable in the enclosing scope (but not the global scope), you can use the nonlocal keyword to indicate that you are referring to the variable in the enclosing scope rather than creating a new local variable. For example:
def outer_func():
    x = 100  # variable in the enclosing scope
    def inner_func():
        nonlocal x  # indicate that we want to use the variable x from the enclosing scope
        x = 200  # modify the variable in the enclosing scope
        print(x)  # Output: 200
    inner_func()
    print(x)  # Output: 200
#outer_func() - In this example, we have an outer function outer_func that defines a variable x with the value 100. Inside outer_func, there is an inner function inner_func that uses the nonlocal keyword to indicate that it wants to refer to the variable x from the enclosing scope (outer_func). We then modify the value of x to 200 inside inner_func. When we call inner_func(), it prints the modified value of x, which is 200. After calling inner_func(), when we print x in outer_func, it also reflects the modified value of 200, demonstrating that we successfully modified the variable in the enclosing scope using the nonlocal keyword.

#The lEGB rule:

#In Python, the LEGB rule is a way to determine the order in which Python looks for variables when they are referenced in a program. The acronym LEGB stands for Local, Enclosing, Global, and Built-in, which represent the four types of scopes that Python uses to resolve variable names.

# Local: Variables defined within the current function
# Enclosing: Variables defined in the enclosing function (if the current function is nested inside another function)
# Global: Variables defined at the top level of the module or script
# Built-in: Names of built-in functions and exceptions that are always available in Python

