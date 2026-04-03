#combined values:

#combined  of the match statement can be used to match multiple values in a single case. for example we can use the match statement to match both "start" and "begin" commands in a single case.

command = input("Enter a command: ")
match command:
    case "start" | "begin":
        print("Starting the engine...") #output: Starting the engine...
    case "stop" | "end":
        print("Stopping the engine...") #output: Stopping the engine...
    case "pause" | "wait":
        print("Pausing the engine...") #output: Pausing the engine...
    case _:
        print("Unknown command.") #output: Unknown command.  

