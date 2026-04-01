#nested if statements: A nested if statement is an if statement that is contained within another if statement. It allows you to check for multiple conditions and execute different blocks of code based on those conditions.


#Example of nested if statement:

age = int(input("enter your age:"))
if age >= 18:
    print("You are eligible to vote.") #output: You are eligible to vote.
    if age >= 21:
        print("You are also eligible to drink alcohol.") #output: You are also eligible to drink alcohol.
    else:
        print("You are not eligible to drink alcohol.") #output: You are not eligible to drink alcohol.             
else:
    print("You are not eligible to vote.") #output: You are not eligible to vote.


#example of nested if statement with multiple conditions:

score = int(input("enter your score:"))
if score >= 90:
    print("You got an A grade.") #output: You got an A grade.
elif score >= 80:
    print("You got a B grade.") #output: You got a B grade.
    if score >= 85:
        print("You got a B+ grade.") #output: You got a B+ grade.
    else:
        print("You got a B- grade.") #output: You got a B- grade.
elif score >= 70:
    print("You got a C grade.") #output: You got a C grade.
elif score >= 60:
    print("You got a D grade.") #output: You got a D grade.
else:
    print("You got an F grade.") #output: You got an F grade.

