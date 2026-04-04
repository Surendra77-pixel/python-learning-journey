#while loop 

#definition: A while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. The loop will continue to execute as long as the condition is true.

#SO NOW WE WILL SEE THE SYNTAX OF THE WHILE LOOP-
#syntax:
#while condition:
    #block of code to be executed

#1.HERE WE PRINT THE NUMBERS FROM 1 TO 5 USING THE WHILE LOOP-
i = 1
while i <= 5:
    print(i) #output: 1 2 3 4 5
    i += 1 #this is the increment operator which is used to increase the value of i by 1 in each iteration of the loop. it is equivalent to i = i + 1. without this line the loop will run indefinitely because the condition will always be true. so it is important to have a way to change the value of the variable that is being used in the condition of the while loop to avoid infinite loops.  
    
#2.writing a loop to print numbers from 10 to 1 in reverse order - 

num=10
while num >=1:
    print(num)
    num -=1
     #this is the decrement operator which is used to decrease the value of num by 1 in each iteration of the loop. it is equivalent to num = num - 1. without this line the loop will run indefinitely because the condition will always be true. so it is important to have a way to change the value of the variable that is being used in the condition of the while loop to avoid infinite loops.
#so we get the output as 10 9 8 7 6 5 4 3 2 1

#3.The basic user login system using the while loop with a maximum of 3 attempts-

user="surendra"
password="manthri"
count = 3

while count > 0:
    username=input("Enter the user name:")
    userpassword=input("enter the password:")

    if user == username and userpassword == password:
        print("The login is succesfull")
        break
        
    else:
        print("invalid try again ")
        count -=1
        if count == 0:
            print("account locked")
            #output:
            #Enter the user name:surendra
            #enter the password:manthri
            #The login is succesfull
#explanation: In this code, we have a while loop that continues to execute as long as the count variable is greater than 0. Inside the loop, we prompt the user to enter their username and password. We then check if the entered username and password match the predefined values. If they do, we print a success message and break out of the loop. If they don't match, we print an error message and decrement the count variable by 1. If the count reaches 0, we print a message indicating that the account is locked.

#4.example of a while loop with some loiacal operators-
Food: str =input("enter the food you like(q to quit):")
while not food == "q":
    print(f"you like {food}")
    food =input("enter the food you like(q to quit):")
    print("bye")
#explanation: In this code, we have a while loop that continues to execute as long as the user does not enter "q". Inside the loop, we print a message indicating the food that the user likes and then prompt them to enter another food. If the user enters "q", the loop will terminate and we will print "bye".

#output:
#enter the food you like(q to quit):pizza
#you like pizza
#enter the food you like(q to quit):burger
#you like burger
#enter the food you like(q to quit):q
#bye

#5. real world example where the while loop is used


# 1. password checking -

# 🔐 Simple Login Program

# Step 1: Store the correct password
# This is the real password saved in the system
password = "1234"

# Step 2: Ask the user to enter a password
# The input given by the user is stored in 'user'
user = input("Enter the password: ")

# Step 3: Start a loop
# This loop runs ONLY when the password is incorrect
# (user != password means "user password is not equal to real password")
while user != password:
    
    # If the password is wrong, print this message
    print("❌ Incorrect password, try again!")
    
    # Ask the user to enter the password again
    user = input("Enter the password: ")

# Step 4: This line runs AFTER the loop ends
# The loop ends only when the correct password is entered
print("✅ Login successful 🎉")

# Wrong password → loop repeats 🔁
# Correct password → loop stops → login success 🎉

#2. a simple code to exit the game loop:

user = input("Do you want to play the game? (yes/no): ")

while not user == "no":
    print("playing the game ...")
    user=input("Do you want to play the game? (yes/no): ")
    print("thanks for playing the game")

