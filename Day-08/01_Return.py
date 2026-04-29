
#Return function------

#The return statement is used to exit a function and go back to the place from where it was called. It can also be used to return a value from a function.

#example:
def adddd(a, b):
    return a + b
result = adddd(5, 3)
print(result) #output: 8

#In this example, the adddd function takes two parameters, a and b, and returns their sum. When we call the function with the arguments 5 and 3, it calculates the sum and returns the value 8, which is then stored in the variable result and printed to the console.

# ----if a function dosent have a return statement, it will return None by default. For example:
def greet(name):
    print(f"Hello, {name}!")
result = greet("Alice")
print(result) #output: Hello, Alice! None

#In this example, the greet function prints a greeting message but does not have a return statement. When we call the function with the argument "Alice", it prints "Hello, Alice!" and then returns None by default, which is stored in the variable result and printed to the console.

#pass -

#The pass statement is a placeholder that does nothing. It is used when you need to define a function or a block of code but don't want to implement it yet. It allows you to create a function without any code inside it, which can be useful for testing or when you are still working on the implementation.

#example:
def my_function():
    pass
#In this example, the my_function is defined but does not contain any code. The pass statement allows us to create the function without causing any errors, and we can later fill in the implementation when we are ready.


#if one return statement is executed, the function will exit immediately and any code after the return statement will not be executed. For example:
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(5))  # Output: Positive
print(check_number(-3)) # Output: Negative
print(check_number(0))  # Output: Zero
#In this example, the check_number function checks if the input number is positive, negative, or zero. Once a return statement is executed, the function exits immediately, and the appropriate message is returned based on the condition.

#The .difference between return and print is that return is used to send a value back to the caller of the function, while print is used to display a message or value on the console. Return allows you to capture the output of a function and use it in other parts of your code, while print is primarily for debugging or providing information to the user.
#example:

def addd(a,b,c):
    return(a+b+c)
result=addd(2,4,4)
print(result) #output: 10

def add(a,b,c):
    print(a+b+c)
result=add(2,4,4)
print(result) #output: 10 None -In the first example, the addd function returns the sum of a, b, and c, which is stored in the variable result and printed to the console. In the second example, the add function prints the sum directly but does not return any value, so when we try to print result, it outputs None because there is no return value from the function.

#note -- 

#1.every function in the python always retirns something if you dont write return the python automatically returns None

