

#                                       try

#In Python, the try statement is used to handle exceptions that may occur during the execution of a block of code. The try block contains the code that may raise an exception, and the except block contains the code that will be executed if an exception occurs. Here is an example of how to use the try statement:

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
#In this example, we are trying to divide two numbers entered by the user. If the user enters zero for num2, a ZeroDivisionError will be raised, and the corresponding error message will be printed. If the user enters a non-integer value for num1 or num2, a ValueError will be raised, and the corresponding error message will be printed. If there are no exceptions, the result of the division will be printed.

# if one try get error the below files will not be executed because the program will jump to the except block of the first try and handle the error there. The second try block will be skipped entirely. For example:

try:
    print("Step 1")
    print(10 / 0)
    print("Step 2")

except:
    print("Error occurred")


#Real time example of try statement:

#bank account example:

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
        except ValueError as e:
            print(e)
account = BankAccount(100)
account.withdraw(150) #output: Insufficient funds (because we are trying to withdraw an amount that is greater than the balance. The withdraw method raises a ValueError with the message "Insufficient funds", which is caught in the except block and printed to the user.)

