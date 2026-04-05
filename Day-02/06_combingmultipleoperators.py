#combing the multiple operators - In Python, you can combine multiple operators in a single expression to perform complex calculations or comparisons. The order of operations follows the standard mathematical rules, which can be modified using parentheses to ensure the desired evaluation order.

#Example of combining multiple operators:

result = (10 + 5) * 2 - 3 / 1
print(result) #Output: 27.0 - The expression is evaluated as follows: First, the parentheses() are evaluated, resulting in 15. Then, the multiplication is performed, resulting in 30. Next, the division is performed, resulting in 3. Finally, the subtraction is performed, resulting in 27.0.


#checking the age for the work eligible:

age=int(input("enter the age:"))
if age<60 and age>18:
    print("Eligible to work")
elif age > 60 :
    print("senior citizen")
else:
    print("Not eligible")
        #output:
        #enter the age:25
        #Eligible to work  


    
#checking the temperature:

temp=int(input("enter the temperature:"))
if temp > 30:
    print("hot")
elif temp >15 and temp < 30:
    print("normal")
else:
    print("cold")
        #output:
        #enter the temperature:20
        #normal

#example-

#. Number Category: #Take a number #If number is divisible by both 3 AND 5 → "FizzBuzz" #If divisible by only 3 → "Fizz" #If divisible by only 5 → "Buzz" #Else → "Other"

num=int(input("enter the number :"))
if num %3==0 and num%5==0:
    print("Fizzbuzz")
elif num %3 == 0:
    print("Fizz")
elif num %5 == 0:
    print("Buzz")
else:
    print("others")
        #output:
        #enter the number :15
        #Fizzbuzz

#example-

#login with attempts:#👉 Ask username and password #If correct → "Login Success" #Else if username correct BUT password wrong → "Wrong Password" #Else → "User Not Found"

username=str(input("enter the user name:"))
password=int(input("enter the password"))
user_name="Surendra"
password_key=1234
if username == user_name and password == password_key:
    print("Login success")
elif username == user_name and password != password_key:
    print("Wrong password")
elif username != user_name and password == password_key:
    print("The password is crt , but the username is wrong")
else:
    print("usernotfound")
        #output:
        #enter the user name:Surendra
        #enter the password:1234
        #Login success .