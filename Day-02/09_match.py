#match:

# The match statement is a powerful control flow structure in Python that allows you to compare a value against a series of patterns and execute code based on which pattern matches. It is similar to a switch-case statement in other programming languages but offers more flexibility and features. The match statement was introduced in Python 3.10.     


#Example of using match statement:

command = input("Enter a command: ")
match command:
    case "start":
        print("Starting the engine...") #output: Starting the engine...
    case "stop":
        print("Stopping the engine...") #output: Stopping the engine...
    case "pause":
        print("Pausing the engine...") #output: Pausing the engine...
    case _:
        print("Unknown command.") #output: Unknown command.


#when the match statement is used ?? - instead of writing the many if-else statements we can use the match statement to make the code more readable and maintainable. it is used when we have multiple conditions to check and we want to execute different blocks of code based on those conditions. it is also used when we want to compare a value against a series of patterns and execute code based on which pattern matches.


#The match expression is evaluted once
#the value of the expression is compared with values in the case statements
#if there is a match then the corresponding block of code is executed
#the match statement can also be used with patterns to extract values from the matched case and use them in the corresponding block of code. for example we can use the match statement to extract the command and the arguments from the input and use them in the corresponding block of code.


#other example of using match statement with patterns:
command = input("Enter a command: ")    
match command.split():
    case ["start", engine]:
        print(f"Starting the {engine} engine...") #output: Starting the {engine} engine...
    case ["stop", engine]:
        print(f"Stopping the {engine} engine...") #output: Stopping the {engine} engine...
    case ["pause", engine]:
        print(f"Pausing the {engine} engine...") #output: Pausing the {engine} engine...
    case _:
        print("Unknown command.") #output: Unknown command.


