class InsufficientBalanceError(Exception):
    pass

# Initial Balance
balance = 5000

try:
    print("Welcome to Python Bank ATM")

    # User input
    amount = int(input("Enter withdrawal amount: "))

    # Validation
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    # Custom Exception
    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance")

    # Successful withdrawal
    balance = balance - amount

except ValueError as e:
    print("Value Error:", e)

except InsufficientBalanceError as e:
    print("Transaction Failed:", e)

else:
    print("Transaction Successful")
    print("Remaining Balance:", balance)

finally:
    print("Thank you for using Python Bank ATM")

#output:
#Welcome to Python Bank ATM
#Enter withdrawal amount: 6000
#Transaction Failed: Insufficient Balance
#Thank you for using Python Bank ATM

#In this example, we have defined a custom exception called InsufficientBalanceError to handle the case when the withdrawal amount exceeds the available balance. The user is prompted to enter a withdrawal amount, and the program checks if the amount is valid and if there are sufficient funds in the account. If any of these conditions are not met, the appropriate exception is raised and handled in the except blocks. If the transaction is successful, the remaining balance is displayed. Finally, a thank you message is printed regardless of whether an exception occurred or not.