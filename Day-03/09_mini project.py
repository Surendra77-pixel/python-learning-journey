# 🏦 BANK SYSTEM

balance = 10000

while True:
    print("\n--- BANK MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please select 1-4.")
        continue
        
    if choice == "1":
        print(f"Your balance is: ₹{balance}")


    elif choice == "2":
        amount = input("Enter deposit amount: ")
        
        if not amount.isdigit():
            print("Invalid amount. Enter numbers only.")
            continue

        amount = int(amount)

        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{balance}")

    elif choice == "3":
        amount = input("Enter withdrawal amount: ")

        if not amount.isdigit():
            print("Invalid amount. Enter numbers only.")
            continue

        amount = int(amount)

        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        if amount > balance:
            print("Insufficient balance.")
            continue

        balance -= amount
        print(f"Withdrawn ₹{amount}. Remaining balance: ₹{balance}")

    elif choice == "4":
        print("Thank you for using the bank system!")
        break

#OUTPUT:
#--- BANK MENU ---
#1. Check Balance
#2. Deposit
#3. Withdraw
#4. Exit
#Enter your choice (1-4): 1
#Your balance is: ₹10000
#--- BANK MENU ---
#1. Check Balance
#2. Deposit
#3. Withdraw
#4. Exit
#Enter your choice (1-4): 2
#Enter deposit amount: 5000
#Deposited ₹5000. New balance: ₹15000
#--- BANK MENU ---
#1. Check Balance
#2. Deposit
#3. Withdraw
#4. Exit
#Enter your choice (1-4): 4
#Thank you for using the bank system!

#explanation: In this code, we have a simple bank system that allows the user to check their balance, deposit money, withdraw money, or exit the program. The while loop continues to run until the user chooses to exit. Inside the loop, we display a menu and prompt the user for their choice. We then use if-elif statements to handle each option. We also include input validation to ensure that the user enters valid choices and amounts. The balance is updated accordingly based on the user's actions. 