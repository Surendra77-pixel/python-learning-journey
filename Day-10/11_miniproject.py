
#                 menu-driven calculator where the user chooses operations.
import math

def show_menu():
    print("\n===== SMART CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Logarithm")
    print("8. Trigonometry (sin, cos, tan)")
    print("9. Exit")

while True:
    show_menu()
    
    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", a / b)

    elif choice == "5":
        num = float(input("Enter number: "))
        print("Square root:", math.sqrt(num))

    elif choice == "6":
        base = float(input("Enter base: "))
        exp = float(input("Enter exponent: "))
        print("Result:", math.pow(base, exp))

    elif choice == "7":
        num = float(input("Enter number: "))
        print("Log value:", math.log(num))

    elif choice == "8":
        angle = float(input("Enter angle (in radians): "))
        print("sin:", math.sin(angle))
        print("cos:", math.cos(angle))
        print("tan:", math.tan(angle))

    elif choice == "9":
        print("Exiting calculator...")
        break

    else:
        print("Invalid choice! Try again.")