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

#positive and the negative number example:

number = int(input("enter a number:"))
if number > 0:
    print("The number is positive.") #output: The number is positive.
    if number % 2 == 0:
        print("The number is also even.") #output: The number is also even.
    else:
        print("The number is also odd.") #output: The number is also odd.   
elif number < 0:
    print("The number is negative.") #output: The number is negative.
    if number % 2 == 0:
        print("The number is also even.") #output: The number is also even.
    else:
        print("The number is also odd.") #output: The number is also odd.
else:
    print("The number is zero.") #output: The number is zero.

#other example of nested if statement:

score = 85
attendance = 90
submitted = True
if score >= 85:
    if attendance >= 90:
        if submitted:
            print("pass")
        else:
            print("pass, but missing submission")
    else:
        print("pass but low attendance")
else:
    print("fail")
    #In this example, the nested if statements check for multiple conditions related to a student's score, attendance, and submission status to determine if they pass or fail.