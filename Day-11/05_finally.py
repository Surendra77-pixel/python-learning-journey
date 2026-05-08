
#                                      finally block

#The finally block is a part of the try-except structure in Python that allows you to specify code that will be executed regardless of whether an exception was raised or not. The code inside the finally block will always run, even if an exception occurs in the try block and is handled by an except block.

#in simple words the finnaly runs no matter what happens in the try block whether there is an exception or not. It is used to ensure that certain cleanup code or important actions are executed, such as closing files, releasing resources, or performing necessary cleanup tasks.

#syantax:

try:
    # code that may raise an exception
except SomeException:
    # code to handle the exception
finally:
    # code that will always be executed

#Here is an example of how to use the finally block:

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("This will always be printed regardless of exceptions.")
#In this example, the finally block will always be executed, regardless of whether an exception occurs in the try block or not. If the user enters valid numbers and no exceptions are raised, the result of the division will be printed, followed by the message from the finally block. If an exception occurs, the corresponding except block will handle the error, and then the finally block will still be executed, printing its message. The finally block is useful for ensuring that certain actions are taken regardless of the outcome of the try block, such as cleaning up resources or providing important information to the user.


try:
    num = int("abc")
    print(num)
except ValueError:
    print("Error")
finally:
    print("This will always be printed")#output: Error This will always be printed (because there is an exception in the try block, so the except block is executed and then the finally block is executed regardless of the exception)


    