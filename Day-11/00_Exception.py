
#                                 Exceptions

#Imagine you are building :

#1.A banking application and you want to ensure that users cannot withdraw more money than they have in their account. You can use exceptions to handle this situation gracefully.

#2.A web application where users can submit forms. If a user submits a form with invalid data (e.g., missing required fields or incorrect formats), you can raise exceptions to inform the user about the errors and prompt them to correct their input.

#3.A file processing application that reads data from files. If the file is not found or cannot be opened, you can raise exceptions to handle these scenarios and provide appropriate error messages to the user.

#Exception handling is a way to manage errors durimg program execution without stopping the program abruptly. It allows you to catch and handle errors gracefully, providing a better user experience and preventing crashes.

#what is an expection? 

#An exception is an error that occurs while the program is running. When an error occurs, Python raises an exception, which can be caught and handled using try-except blocks.

#Example of exception handling:
a = 10
b = 0
print(a / b) output: ZeroDivisionError: division by zero
#explanation: In this example, we are trying to divide a number by zero, which is not allowed in mathematics. When we run this code, Python raises a ZeroDivisionError exception because it cannot perform the division operation. To handle this exception, we can use a try-except block.


#Real-time example-


#1.lets see the Atm machine example:

#suppose :

#1.user had insufficient funds in their account
#2.user entered an invalid pin number
#3.server is down  ---At this point the atm dosent crash but it shows a message to the user that the server is down and to try again later. and continue running

try:
    amount = int(input("Enter amount: "))
    print(1000 / amount)

except ZeroDivisionError:
    print("Amount cannot be zero")


#2.Instagram login-

#suppose:
#1.user enters wrong username or password
#2.server is down
#3.no internet connection  --- in this case instgram handles the exception by showing a message to the user that there is no internet connection and to try again later. and continue running

#Basic study of exception handling:

try:
    # risky code
except:
    # handling the error



#Rules in the exception handling:

#1.The code that may raise an exception is placed inside the try block.

#2.If an exception occurs, the code inside the except block is executed to handle the error.

#3.If no exception occurs, the except block is skipped.

#4.You can have multiple except blocks to handle different types of exceptions.

#5.You can also use a generic except block to catch any type of exception, but it is generally recommended to catch specific exceptions for better error handling.

#6.only one generic- means expect is used only onces and it should be the last one in the sequence of except blocks.

#7.if the one try gets the error below the below that try will not be executed because the program will jump to the except block of the first try and handle the error there. The second try block will be skipped entirely.

#8.The exception handling doesnt stop the entire program it handles the error and allows the program to continue safely without crashing.

#9.except runs only when there is an error in the try block. If there is no error, the except block will be skipped and the program will continue executing the code after the try-except structure.

#10.one try can have the multiple except blocks to handle different types of exceptions. This allows you to provide specific error handling for different types of errors that may occur in the try block. Each except block can catch a specific type of exception, allowing you to handle each error case appropriately.

#for example:
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")


#11.The except block from the top to bottom the first matching exception executes for example:
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
#In this example, if the user enters zero for num2, the ZeroDivisionError will be caught and the corresponding error message will be printed. If the user enters a non-integer value for num1 or num2, the ValueError will be caught and the corresponding error message will be printed. If there are no exceptions, the result of the division will be printed.



#There are different types of exceptions in python- 

#1.try

#2.except

#3.else

#4.finally

#5.raise

#6.assert

#7.with statement

#8.custom exceptions

#9. built-in exceptions

#10.expection as e

#Imagine driving a car Seatbelt = Exception Handling Accident may or may not happen But protection is necessary Similarly:Errors may or may not occur Exception handling protects the program

#in real software companies:

#exception handling is everywhere APIs use it,banking apps use it ,AI systems use it ,cloud servers use it ,Without exception handling: ,software becomes unstable ,users lose trust