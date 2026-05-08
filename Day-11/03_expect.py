
#                         except 

#In Python, the except statement is used to catch and handle exceptions that may occur during the execution of a block of code. It is used in conjunction with the try statement to define a block of code that may raise an exception and a block of code that will be executed if an exception occurs. Here is an example of how to use the except statement:

try:
    print(5 / 0)

except:
    print("Error handled")#output: Error handled
#In this example, we are trying to divide a number by zero, which is not allowed in mathematics. When we run this code, Python raises a ZeroDivisionError exception because it cannot perform the division operation. The except block catches the exception and prints the message "Error handled". This allows the program to continue running without crashing, even though an error occurred.

#You can also specify the type of exception you want to catch in the except block. For example:

try:
    print(5 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")#output: Cannot divide by zero
#In this example, we are catching the specific ZeroDivisionError exception and printing a more specific error message. This is generally recommended for better error handling, as it allows you to provide more specific feedback to the user and handle different types of exceptions in different ways.  

#Exception handling is a mechanism used to handle runtime errors and prevent program termination.

#generic except block:
try:
    print(5 / 0)
except:
    print("An error occurred")#output: An error occurred


#specific except block:
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")#output: Cannot divide by zero


#The mutiple except block if given then  it will only execute the first except block that matches the type of exception raised. If an exception is raised that does not match any of the specified except blocks, it will be caught by a generic except block if one is provided, or it will propagate up the call stack if no generic except block is present. For example:
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")#output: Cannot divide by zero
except ValueError:
    print("Invalid value")
except:
    print("An error occurred")
#In this example, the ZeroDivisionError exception is raised, and the first except block that matches this exception is executed, which prints "Cannot divide by zero". The other except blocks are not executed because the exception has already been handled. If we were to raise a different type of exception, such as a ValueError, then the second except block would be executed instead. If an exception is raised that does not match any of the specified except blocks, then the generic except block would be executed, printing "An error occurred".


try:
    num = int("abc")
    print(num)

except ValueError:
    print("Invalid conversion")

print("Program ended")


try:
    print("A")
    print(10 / 2)
    print("B")

except ZeroDivisionError:
    print("Error")

print("C")

#In this example, the code inside the try block will execute without any exceptions, so the except block will be skipped. The output will be:
A
5.0
B
C

#the simple doubt every one gets is why the print c is executed even when there is an error in the try block. The reason is that the except block only handles the specific exception that occurs in the try block, and once the exception is handled, the program continues to execute the code after the try-except structure. In this case, since there is no exception raised in the try block, the except block is skipped, and the program continues to execute the print("C") statement, resulting in "C" being printed to the output.

try:
    print("Start")
    print(10 // 0)
    print("Middle")

except ZeroDivisionError:
    print("Cannot divide")

print("End") 

#0utput:
#Start
#Cannot divide
#End

try block
   ↓
ZeroDivisionError occurs
   ↓
ValueError?
   ↓
ZeroDivisionError? 
   ↓
Execute matching except


