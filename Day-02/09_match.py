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
        print("Unknown command.") #output: Unknown command.


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


#the match with the if statement:

month=5
day=5
match day:
    case 1 | 21 | 31:
        suffix="st"
    case 5 | 22 if month == 5:
        suffix="nd"
        suffix="5th"
    case 3 | 23:
        suffix="rd"
    case _:
        suffix="th"
print(f"{day}{suffix} of month {month}{suffix}") #output: 5th of month 5th


#suffix -A suffix is a group of letters added to the end of a word to change its meaning or function. in the context of the match statement, a suffix is used to indicate the ordinal number of a day in a month. for example, the suffix "st" is used for the 1st, 21st, and 31st days of a month, while the suffix "nd" is used for the 2nd and 22nd days of a month. the suffix "rd" is used for the 3rd and 23rd days of a month, and the suffix "th" is used for all other days of a month.


# Match-Case with Logical Operators In Python match-case, you cannot directly use and, or, not like in if BUT you can achieve similar behavior using:
 
#using and-

age = int(input("Enter age: "))
status = input("Enter status (student/worker): ")

match (age, status):
    case (a, s) if a > 18 and s == "student":
        print("Eligible student adult")
    case _:
        print("Not eligible")
        #output:
        #Enter age: 20
        #Enter status (student/worker): student
        #Eligible student adult
        #explanation: In this example, we are using a tuple (age, status) to match against the cases. The first case checks if the age is greater than 18 and the status is "student". If both conditions are true, it prints "Eligible student adult". The second case is the default case that matches anything that doesn't match the first case, and it prints "Not eligible".  

#example 2: using or-

num = int(input("Enter a number: "))
match num:
    case n if n == 0 or n == 1:
        print("Binary digit")
    case _:
        print("Not binary")
        #output:
        #Enter a number: 1  
        #Binary digit
        #explanation: In this example, we are using a single variable num to match against the cases. The first case checks if num is either 0 or 1 using the logical operator or. If num is 0 or 1, it prints "Binary digit". The second case is the default case that matches anything that doesn't match the first case, and it prints "Not binary".

#using not -

x = int(input("Enter number: "))

match x:
    case n if not n > 0:
        print("Non-positive number")
    case _:
        print("Positive number")
        #output:
        #Enter number: -5   
        #Non-positive number
        #explanation: In this example, we are using a single variable x to match against the cases. The first case checks if x is not greater than 0 using the logical operator not. If x is not greater than 0, it prints "Non-positive number". The second case is the default case that matches anything that doesn't match the first case, and it prints "Positive number".


#Match-Case with Membership Operators (in, not in) -

#- very useful when you want to check if a value is present in a collection (like a list, tuple, or set) within a match-case statement.

#using in operator:
fruit = input("Enter fruit: ")

match fruit:
    case f if f in ["apple", "banana", "mango"]:
        print("This is a common fruit")
    case _:
        print("Unknown fruit")
        #output:
        #Enter fruit: apple 
        #This is a common fruit
        #explanation: In this example, we are using a single variable fruit to match against the cases. The first case checks if fruit is in the list ["apple", "banana", "mango"] using the membership operator in. If fruit is one of those three fruits, it prints "This is a common fruit". The second case is the default case that matches anything that doesn't match the first case, and it prints "Unknown fruit".


#exmple 2: using not in operator:
char = input("Enter a character: ")

match char:
    case c if c not in "aeiou":
        print("Consonant")
    case _:
        print("Vowel")
        #output:
        #Enter a character: b
        #Consonant
        #explanation: In this example, we are using a single variable char to match against the cases. The first case checks if char is not in the string "aeiou" using the membership operator not in. If char is not a vowel (i.e., it is a consonant), it prints "Consonant". The second case is the default case that matches anything that doesn't match the first case, and it prints "Vowel".


#example  membership operator with numbers:
num = int(input("Enter number: "))

match num:
    case n if n in range(1, 11):
        print("Between 1 and 10")
    case _:
        print("Out of range")
        #output:
        #Enter number: 5
        #Between 1 and 10
        #explanation: In this example, we are using a single variable num to match against the cases. The first case checks if num is in the range from 1 to 10 (inclusive) using the membership operator in with the range function. If num is between 1 and 10, it prints "Between 1 and 10". The second case is the default case that matches anything that doesn't match the first case, and it prints "Out of range".

