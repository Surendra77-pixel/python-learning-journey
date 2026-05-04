#else:in simple when the if and elif condition is not satisfied then the else block will be executed. it is used to execute a block of code when all the conditions are false. it is optional and can be used with if statement or if-elif statement. without if when you try the else statement it will give you an error or empty  

#example of using else statement:

a=int(input("enter the number"))
balance=1000
if a > balance:
    print("you have insufficient balance")
else:
    print("you have sufficient balance")
        #output:
        #enter the number 1500
        #you have insufficient balance

#else fallback: it is used to execute a block of code when all the conditions are false. it is optional and can be used with if statement or if-elif statement. without if when you try the else statement it will give you an error or empty. it is used to provide a default case when all the conditions are false.

username="surendra"
if len(username) < 5:
    print("username is too short")
else:
    print("username is valid")
        #output:
        #username is valid .