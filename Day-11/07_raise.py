

#                          raise statement in python

#raise is used to manually generate an exception.raise allows programmers to create errors intentionally.

#The raise statement in Python is used to manually trigger an exception. It allows you to create and raise your own exceptions or re-raise existing exceptions. The syntax for the raise statement is as follows:
 
#syantax:
raise Exception("Error message")
 
age = -5
if age < 0:
    raise ValueError("Age cannot be negative") #output: ValueError: Age cannot be negative (because we are checking if the age is negative, and if it is, we raise a ValueError with a custom error message. When this code is executed, it will raise the ValueError exception, and the program will terminate unless the exception is caught and handled by an except block.)

#Here is an example of how to use the raise statement:

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
#In this example, we are checking if the age is negative. If it is, we raise a ValueError with a custom error message. When this code is executed, it will raise the ValueError exception, and the program will terminate unless the exception is caught and handled by an except block.

try:
    age = -1

    if age < 0:
        raise ValueError("Invalid age")
except Exception as e:
    print(e)
 #output: Invalid age (because we are catching the exception raised by the raise statement using a try-except block. When the ValueError is raised, it will be caught by the except block, and the error message "Invalid age" will be printed to the console.)


#realtime example of raise statement:

password = "123"

if len(password) < 6:
    raise ValueError("Password too short") #output: ValueError: Password too short (because we are checking if the length of the password is less than 6 characters. If it is, we raise a ValueError with a custom error message. When this code is executed, it will raise the ValueError exception, and the program will terminate unless the exception is caught and handled by an except block.)

password = "123"

try:
    if len(password) < 6:
        raise ValueError("password is incorrect")

except Exception as e:
    print(e)

finally:
    print("yes") #output: password is incorrect
#yes (because we are checking if the length of the password is less than 6 characters. If it is, we raise a ValueError with a custom error message. When this code is executed, it will raise the ValueError exception, and the program will jump to the except block where the error message "password is incorrect" will be printed. After handling the exception, the finally block will be executed, which will print "yes" to the console. The finally block is executed regardless of whether an exception was raised or not, so it will always run after the try-except block.)


#using the try , except block to catch the exception raised by the raise statement:

try:
    age = -1

    if age < 0:
        raise ValueError("Invalid age")

except Exception as e:
    print(e)#output: Invalid age (because we are catching the exception raised by the raise statement using a try-except block. When the ValueError is raised, it will be caught by the except block, and the error message "Invalid age" will be printed to the console.) and the program will continue to execute after handling the exception. If there were any code after the except block, it would be executed as well. In this case, since there is no code after the except block, the program will simply end after printing the error message.if i not gave the except block, the program will terminate with an error message when the exception is raised. However, by using a try-except block, we can catch the exception and handle it gracefully, allowing the program to continue running even after an error occurs.

#clearly, the raise statement is a powerful tool in Python that allows you to create and raise exceptions intentionally. It can be used to enforce certain conditions in your code and provide meaningful error messages when those conditions are not met.

#The raise statement can be stops the current block -

try:
    print("A")

    raise ValueError("Error")

    print("B")

except Exception as e:
    print(e) #output: A
#Error (because the raise statement will stop the execution of the current block and jump to the except block when an exception is raised. In this example, the print statement "A" will be executed, but once the raise statement is encountered, it will raise a ValueError and jump to the except block, where the error message "Error" will be printed. The print statement "B" will not be executed because the raise statement has already interrupted the flow of the program.)


#common exceptions that can be raised using the raise statement:

#1.value error:

# This occurs when a function receives an argument of the correct type but an inappropriate value. For example:

age = -5
if age < 0:
    raise ValueError("Age cannot be negative") #output: ValueError: Age cannot be negative (because we are checking if the age is negative, and if it is, we raise a ValueError with a custom error message. When this code is executed, it will raise the ValueError exception, and the program will terminate unless the exception is caught and handled by an except block.) 

#2.type error:

# This occurs when an operation or function is applied to an object of inappropriate type. For example:
a = "10"
b = 5
print(a + b) #output: TypeError: can only concatenate str (not "int") to str (because we are trying to add a string and an integer, which is not allowed in Python. When this code is executed, it will raise a TypeError exception.


#3.permission error:

# This occurs when trying to perform an operation that requires special permissions. For example:
import os
os.remove("file.txt") #output: PermissionError: [Errno 13] Permission denied: 'file.txt' (because we are trying to remove a file that we do not have permission to access. When this code is executed, it will raise a PermissionError exception.)


#4runtime error:
# This occurs when an error is detected that doesn't fall in any of the other categories. For example:
a = 10
b = 0
print(a / b) #output: ZeroDivisionError: division by zero (because we are trying to divide a number by zero, which is not allowed in mathematics. When this code is executed, it will raise a ZeroDivisionError exception.)

try:
    number = -10

    if number < 0:
        raise ValueError("Negative numbers not allowed")

    print(number)

except Exception as e:
    print("Caught:", e)

print("Program Ended")

#output: Caught: Negative numbers not allowed
#Program Ended (because we are trying to raise a ValueError when the number is negative. The exception is caught in the except block, and the error message "Negative numbers not allowed" is printed. After handling the exception, the program continues to execute and prints "Program Ended".)

#The raise statemnet is mainly used for the validation of the data. It is used to check if the data is valid or not, and if it is not valid, it raises an exception with a custom error message. This allows us to handle the exception in a way that is appropriate for our application.

#real time validation examples-

#1.login system:
username = "admin"
password = "123"
if username != "admin" or password != "123":
    raise ValueError("Invalid username or password") #output: ValueError: Invalid username or password (because we are checking if the username and password are correct. If they are not, we raise a ValueError with a custom error message. When this code is executed, it will raise the ValueError exception, and the program will terminate unless the exception is caught and handled by an except block.)

#2.banking system:

balance = 1000
withdrawal_amount = 1500
if withdrawal_amount > balance:
    raise ValueError("Insufficient funds") #output: ValueError: Insufficient funds (because we are checking if the withdrawal amount is greater than the balance. If it is, we raise a ValueError with a custom error message. When this code is executed, it will raise the ValueError exception, and the program will terminate unless the exception is caught and handled by an except block.)

#3.api validation:

def get_user_info(user_id):
    if user_id <= 0:
        raise ValueError("Invalid user ID") #output: ValueError: Invalid user ID (because we are checking if the user ID is valid. If it is not, we raise a ValueError with a custom error message. When this code is executed, it will raise the ValueError exception, and the program will terminate unless the exception is caught and handled by an except block.)