#elif -The elif statement is used in conditional statements to check multiple conditions. It stands for "else if" and allows you to check for additional conditions if the previous conditions were not true. inshort form we can say that if condition is worong then we can use the multiple conditions using elif statement.

#Example of using elif statement:

age = int(input("enter your age:"))
if age < 18: 
    print("You are a minor.") #output: You are a minor.
elif age < 65:
    print("You are an adult.") #output: You are an adult.
else:
    print("You are a senior citizen.") #output: You are a senior citizen.

#now we will print the multiple conditions using elif statement:

score = int(input("enter your score:"))
if score >= 90:
    print("You got an A grade.") #output: You got an A grade.   
elif score >= 80:
    print("You got a B grade.") #output: You got a B grade.
elif score >= 70:
    print("You got a C grade.") #output: You got a C grade.
elif score >= 60:
    print("You got a D grade.") #output: You got a D grade.     
else:
    print("You got an F grade.") #output: You got an F grade.

#note- only the first true condition will be executed and the rest of the conditions will be ignored. if all conditions are false then the else block will be executed. for example if the score is 85 then only the second condition will be executed and the rest of the conditions will be ignored. if the score is 50 then only the last condition will be executed and the rest of the conditions will be ignored.

