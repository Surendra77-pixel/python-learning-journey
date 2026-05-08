
#                               else

#The else block is used in conjunction with the try-except block to specify a block of code that will be executed if no exceptions are raised in the try block. It allows you to define a section of code that will run only when the try block executes successfully without any errors.

#in simple words, the else block is executed when there is no exception (error) in the try block. It is a way to separate the code that should run when everything goes well from the code that handles exceptions.

#syntax:

try:
    # code that may raise an exception
except SomeException:
    # code to handle the exception
else:
    # code to run if no exceptions were raised

#Here is an example of how to use the else block:
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print("Result:", result)#`output: Result: 5.0 (if the user enters valid numbers and no exceptions are raised)
else:
    print("This will not be printed if there is an exception in the try block.")

  #output: This will not be printed if there is an exception in the try block. (if there is an exception in the try block)if there is no exception in the try block then it will print the above line. If there is an exception in the try block then it will not print the above line because the program will jump to the except block and handle the error there. The else block will be skipped entirely.
    
#In this example, if the user enters valid numbers and no exceptions are raised, the else block will be executed, and the result of the division will be printed. If an exception occurs, the corresponding except block will handle the error, and the else block will be skipped. The else block is useful for code that should only run when the try block is successful, allowing you to keep the error handling code separate from the main logic of your program.

#The else is heavily used in

#1.login systems
#2.payment processing
#3.api calls
#4.data processing

try:
    num = int("20")
    print(num)

except ValueError:
    print("Error")

else:
    print("Success")

print("End") #output: 20 Success End (because there is no exception in the try block, so the else block is executed and then the program continues to print "End")

#if the error occurs in the try block then the else block will not be executed and it will jump to the except block and handle the error there. For example:

try:
    num = int("abc")
    print(num)
except ValueError:
    print("Error") #output: Error (because there is an exception in the try block, so the except block is executed and the else block is skipped)
else:
    print("Success")
print("End") #output: End (because the program continues to print "End" after handling the exception)

