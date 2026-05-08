
#                    Custom Exceptions in Python

#In Python, you can create your own custom exceptions by defining a new class that inherits from the built-in Exception class. This allows you to create specific exceptions that are relevant to your application and provide more meaningful error messages when those exceptions are raised.

#in simple words. this is the user defined exception created by the programmer 



#syntax for creating a custom exception:

from curses import error


class MyError(Exception):
    pass

#Here is an example of how to create and use a custom exception:  


 class InvalidAgeError(Exception):
    pass

age = -5

if age < 0:
    raise InvalidAgeError("Age cannot be negative") #output: InvalidAgeError: Age cannot be negative (because we are creating a custom exception called InvalidAgeError that inherits from the built-in Exception class. We then check if the age is negative, and if it is, we raise the InvalidAgeError with a custom error message. When this code is executed, it will raise the InvalidAgeError exception, and the program will terminate unless the exception is caught and handled by an except block.) 

#In this example, we are creating a custom exception called InvalidAgeError that inherits from the built-in Exception class. We then check if the age is negative, and if it is, we raise the InvalidAgeError with a custom error message. When this code is executed, it will raise the InvalidAgeError exception, and the program will terminate unless the exception is caught and handled by an except block.

class NegativeAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age cannot be negative.")    
#output: Invalid age: -5. Age cannot be negative. (because we are creating a custom exception called NegativeAgeError that inherits from the built-in Exception class. We define an __init__ method to initialize the age attribute and provide a custom error message when the exception is raised. When we check if the age is negative and raise the NegativeAgeError, it will display the custom error message with the invalid age value.)

#1.why class NegativeAgeError(Exception): is used instead of class NegativeAgeError: because we want to create a custom exception that inherits from the built-in Exception class. By inheriting from Exception, our custom exception can be caught and handled like any other exception in Python. If we were to define the class without inheriting from Exception, it would not be recognized as an exception and would not be able to be caught by except blocks that are designed to catch exceptions. Inheriting from Exception allows us to create a custom exception that can be used in the same way as built-in exceptions, providing more flexibility and functionality in our error handling.



#large companys create a many custom exceptions to handle specific error scenarios in their applications. For example, a banking application might have custom exceptions for insufficient funds, invalid account numbers, or unauthorized access. By creating custom exceptions, developers can provide more specific error messages and handle different types of errors in a more organized way. Custom exceptions can also help improve the readability and maintainability of the code by clearly indicating the type of error that occurred.

#PaymentFailedError,AuthenticationError,DatabaseConnectionError,APIKeyExpiredError This makes:debugging easier ,logs cleaner ,code more professional

#memory trick for custom exceptions:

Custom Exception = Your own error type

