
#                         exception handling in python

#The exception handling in Python is a mechanism to handle runtime errors and prevent program termination. It allows you to write code that can gracefully handle errors and continue executing without crashing the program. The main components of exception handling in Python are the try, except, else, and finally blocks.

try:
    print(10 / 0)

except Exception as e:
    print(e)

#output: division by zero (because we are trying to divide a number by zero, which is not allowed in mathematics. When we run this code, Python raises a ZeroDivisionError exception because it cannot perform the division operation. The except block catches this exception and prints the error message "division by zero". The program continues to execute without crashing, allowing us to handle the error gracefully.)

#it says which is the type of the error occured and what is the error message. In this case, it is a ZeroDivisionError and the message is "division by zero". This allows us to understand what went wrong in our code and take appropriate action to fix it.

#in the above code the except block is catching the exception and printing the error message. The variable 'e' is used to store the exception object, which contains information about the error that occurred. By printing 'e', we can see the specific error message associated with the exception, which helps us understand what went wrong in our code.

try:
    x = int("abc")

except Exception as e:
    print("Error message is:", e)

print("Program Ended")

#output: Error message is: invalid literal for int() with base 10: 'abc' Program Ended (because we are trying to convert a string that cannot be converted to an integer, which raises a ValueError exception. The except block catches this exception and prints the error message "invalid literal for int() with base 10: 'abc'". The program continues to execute and prints "Program Ended" without crashing, allowing us to handle the error gracefully.)


