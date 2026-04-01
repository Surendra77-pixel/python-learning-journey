
# Smart CLI Assistant

print("=== Smart CLI Assistant ===")

command = input("Enter command: ").lower()

# Match-case for command handling
match command.split():

    # 🚗 START ENGINE
    case ["start", vehicle]:
        if vehicle in ["car", "bike", "bus"]:  # membership operator
            print(f"Starting the {vehicle}...")
        else:
            print("Unknown vehicle")

    # 🛑 STOP ENGINE
    case ["stop", vehicle]:
        print(f"Stopping the {vehicle}...")

    # 🎂 AGE CHECKER
    case ["check", "age", age]:
        age = int(age)

        if age < 18:
            print("Minor")
        elif age >= 18 and age <= 60:   # logical operator
            print("Adult")
        else:
            print("Senior Citizen")

    # 🔐 LOGIN SYSTEM (Nested IF)
    case ["login", username]:
        password = input("Enter password: ")

        if username == "admin":
            if password == "1234":
                print("Login successful")
            else:
                print("Wrong password")
        else:
            print("User not found")

    # ⚡ QUICK CHECK (Shorthand IF)
    case ["status", number]:
        number = int(number)
        print("Even" if number % 2 == 0 else "Odd")

    # 🚧 FUTURE FEATURE
    case ["update"]:
        pass  # placeholder for future feature

    # ❌ DEFAULT CASE
    case _:
        print("Invalid command")



        