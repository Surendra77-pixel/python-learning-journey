
#ATM Bank Login + Withdrawal System
# Requirements Covered
# login attempts
# Successful login → go to withdrawal
# Retry if insufficient balance
# Exit safely

# BANK SYSTEM

# Step 1: Account details
correct_password = "1234"
balance = 5000

# Step 2: Login system (3 attempts)
attempts = 3

while attempts > 0:
    user_password = input("Enter your password: ")

    if user_password == correct_password:
        print(" Login successful\n")
        break
    else:
        attempts -= 1
        print(f" Wrong password. Attempts left: {attempts}")

# Step 3: If login failed
if attempts == 0:
    print(" Account locked")
else:
    # Step 4: Withdrawal system
    while True:
        print(f"\n Your balance: {balance}")
        amount = int(input("Enter amount to withdraw (0 to exit): "))

        # Exit condition
        if amount == 0:
            print(" Exiting... Thank you!")
            break

        # Check balance
        if amount <= balance:
            balance -= amount
            print(f" Withdrawal successful. Remaining balance: {balance}")
        else:
            print(" Insufficient balance. Try again.")


#OUTPUT:
#Enter your password: 1111
#❌ Wrong password. Attempts left: 2
#Enter your password: 2222
#❌ Wrong password. Attempts left: 1
#Enter your password: 3333
#❌ Wrong password. Attempts left: 0
#🚫 Account locked
#Enter your password: 1234
#✅ Login successful
#WITHDRAWAL SYSTEM
#💰 Your balance: 5000
#Enter amount to withdraw (0 to exit): 6000
#❌ Insufficient balance. Try again.
#💰 Your balance: 500
#Enter amount to withdraw (0 to exit): 0
#👋 Exiting... Thank you!


#EXPLANATION: In this code, we have a simple ATM bank login and withdrawal system. The user has 3 attempts to enter the correct password. If they fail to enter the correct password within 3 attempts, their account is locked. If they successfully log in, they can withdraw money from their account. The user can continue to withdraw money until they choose to exit by entering 0. If they try to withdraw more money than their balance, they will receive an error message and can try again.