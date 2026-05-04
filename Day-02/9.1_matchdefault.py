#default case:

# in match statement is represented by the underscore (_) which matches anything that hasn't been matched by the previous cases. it is similar to the else block in if-else statements. it is used to handle cases where the input does not match any of the specified patterns.


#example of the default case in match statement:

command = input("Enter a command: ")
match command:
    case "start":
        print("Starting the engine...") #output: Starting the engine...
    case "stop":
        print("Stopping the engine...") #output: Stopping the engine...
    case "pause":
        print("Pausing the engine...") #output: Pausing the engine...
    case _:
        print("Unknown command.") #output: Unknown command..