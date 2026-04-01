#This is the assignment of the miniproject im going to implememt now which i had been learned in the day 1 of the python programming language. I will be using the operators, escape strings and format strings in this miniproject.    

#the project im doing now is used to create the simple formatted card that includes the name , age , city ,hobby of the user and also the card will be decorated with some of the escape strings and operators.

#Taking the user input for the card details-

name=input("Enter your name: ")
age=int(input("Enter your age: "))
city=input("Enter your city: ")
hobby=input("Enter your hobby: ")

#printing the formatted card using f-strings and escape strings-
print("\n" + "="*30) # This will print a line of 30 asterisks to decorate the card
print("     user information card") # This will print the title of the card
print("="*30) # This will print another line of 30 asterisks to decorate the card
print(f"Name: {name}") # This will print the name of the user
print(f"Age: {age}") # This will print the age of the user
print(f"City: {city}") # This will print the city of the user
print(f"Hobby: {hobby}") # This will print the hobby of the user
print("="*30) # This will print another line of 30 asterisks to decorate the card