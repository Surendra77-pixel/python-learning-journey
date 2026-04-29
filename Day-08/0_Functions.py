 #FUNCTIONS --------


#A A function is a reusable block of code or programming statements designed to perform a specific task. To define or declare a function, Python provides the def keyword. 

#() - Parentheses are used to enclose the parameters or arguments that a function can take. If a function does not require any parameters, you can simply use empty parentheses.

#a function can be as many times as you want, and you can call it whenever you need to perform the task it is designed for. Functions help in breaking down complex problems into smaller, more manageable pieces, making code easier to read and maintain.


#Real world examples of where the function is used:

#1. In a calculator application, you might have functions for addition, subtraction, multiplication, and division. Each function would take two numbers as input and return the result of the operation.

#2. In a web application, you might have a function to handle user authentication. This function would take a username and password as input, check them against a database, and return whether the login was successful or not.

#3. In a data analysis script, you might have a function to calculate the average of a list of numbers. This function would take a list as input and return the average value.


#rules in defining a function:
#1. A function name must start with a letter (a-z, A-Z) or an underscore (_). It cannot start with a number.

#2. A function name can only contain letters, numbers, and underscores. It cannot contain spaces or special characters.

#3. A function name cannot be a reserved keyword in Python (e.g., def, return, if, else, etc.).

#4. A function name should be descriptive and meaningful to indicate what the function does. This is not a strict rule, but it is a good practice to improve code readability.

#creating a function:

def my_function():
    print("This is the function")
my_function() #output: This is the function

#explanation: In this example, we defined a function called my_function that prints a message when called. We then called the function using its name followed by parentheses, which executed the code inside the function and produced the output "This is the function".

#calling a function:

#To call a function, you simply use the function name followed by parentheses. If the function requires parameters, you would include the appropriate arguments within the parentheses.

#example:
def greet(name):
    print(f"Hello, {name}!")
greet("Alice") #output: Hello, Alice!

#you can call the function multiple times with different arguments and you can call the function as many times as you want, and it will execute the code inside the function each time it is called. For example:
greet("Bob") #output: Hello, Bob!
greet("Charlie") #output: Hello, Charlie!


#when to use the functions:

#imagine you need to convert temperatures from fahrenheit to celsius several times in your program . without functions , you would have to write the same caluculation code repeatedly-

temp1=77
celsius1=(temp1-32)*5/9
print(celsius1)

temp1=95
celsius1=(temp1-32)*5/9
print(celsius1)

temp1=50
celsius1=(temp1-32)*5/9
print(celsius1)


#with functions, you can define a function to perform the conversion and then call it whenever needed, which makes your code cleaner and more efficient:

def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * 5 / 9
print(fahrenheit_to_celsius(77)) #output: 25.0
print(fahrenheit_to_celsius(95)) #output: 35.0
print(fahrenheit_to_celsius(50)) #output: 10.0


