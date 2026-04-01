#1. Positive, Negative or Zero-
#Take a number from the user and print:"Positive" if > 0 ,"Negative" if < 0 ,"Zero" if = 0-

user = int(input("enter the number :"))
if user > 0:
    print("The number is positive ")
if user < 0:
    print("The number is the negative")
else:
    print("The ouput is zero")
        #output:
        #enter the number :-5
        #The number is the negative


#Check if a number is even or odd-

num=int(input("enter any number:"))
if num %2 == 0:
    print("The given number is the even number ")
else:
    print("The given number is the ood number")
        #output:
        #enter any number:5
        #The given number is the ood number


#checking if the person is eligible for the vote or not-

age =int(input("enter your age:"))
if age > 18 :
    print("you age {} is eligible for the vote".format(age))
else:
    print("sorry your{} is not eligible for the vote".format(age))
        #output:
        #enter your age:20
        #you age 20 is eligible for the vote   
        #enter your age:17
        #sorry your17 is not eligible for the vote


#finding largest amoung three numbers-

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a >b and a > c:
    print("The a {} is the largest.".format(a))
elif b>c:
    print("The b {} is largest".format(b))
else:
    print("largest c {} is the largest".format(c))
        #output:
        #enter the number5
        #enter the number10
        #enter the number15
        #largest c 15 is the largest


#checking the grade system-

user=int(input("enter the marks:"))
if user>=90:
    print("The student is passed with grade A")
elif user >= 75:
    print("The student is passed with grade b")
elif user >= 50:
    print("The student is passed with grade c")
else:
    print("The student is fail in the exam due to low marks")
        #output:
        #enter the marks:80
        #The student is passed with grade b
    

#checking if the number is divisible by the 3 and 5-

user=int(input("enter the number: "))
if user % 3 == 0 and user % 5 == 0:
    print("Divisible by both")
else:
    print("no its not divisible by bot")
        #output:
        #enter the number: 15
        #Divisible by both  


#printing the leap year-

year=int(input("enter the leap year:"))
if (year %4==0 and year % 100!=0) or (year % 400 ==0):
    print("The leap year")
else:
    print("not a leap year")
        #output:
        #enter the leap year:2020
        #The leap year
        

##Simple Login System-

username ="Admin"
password="1234"
condition1 =str(input("enter the username:"))
condition2=int(input("enter the password:"))
if condition1 == username:
    print("The login is succesfull")
else:
    print("The login is unsuccesfull")
        #output:
        #enter the username:Admin
        #enter the password:1234
        #The login is succesfull


# number range classifier-

user=int(input("enter the number:"))
if 0<= user <=10:
    print("Low")
elif 11 <= user <=50:
    print("medium")
else:
    print("high")
        #output:
        #enter the number: 5
        #Low


##triangle checker-

a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print("Equilateral")
elif a==b==c or a==c:
    print("sSoscelses")
else:
    print("scalene")
        #output:
        #3
        #3
        #3
        #Equilateral


#ATM withdrawwal system -

balance=1000
withdraw=int(input("enter the amount you need to withdraw:"))
if withdraw>1000:
    print("sorry there is insuffient balance in your accounr")
else:
    balance -= withdraw
    print("remaing balance:",balance)   
        #output:
        #enter the amount you need to withdraw:500
        #remaing balance: 500   

#Electricity bill calculator-

unit=int(input("enter the units used:"))
if unit <= 100:
    print(unit*5)
elif unit<=200:
    print(unit*7)
else:
    print(unit * 10)
        #output:
        #enter the units used:150
        #1050