#Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

x=5 -- This is an integer variable that holds the value 5.
y="python is awesome" -- This is a string variable that holds the value "python is awesome".
X=[1,2,3,4,5] -
X={"Name":"Surendra","Age":30} -- This is a dictionary variable that holds key-value pairs.
X=(1,2,3,4,5) -- This is a tuple variable that holds an ordered collection of values.
X=(20.5,30.5,40.5)-
X=True / False -- This is a boolean variable that can hold either True or False.
X=None -- This is a variable that holds the value None, which represents the absence of a value.


#It has a name to identify it
#Its value can change anytime
#It is created when you assign a value
#It can hold different types of data (e.g., numbers, strings, lists, etc.)
#It can be used to store and manipulate data in a program
#In the above example, 'x' is a variable that holds the integer value 5, and 'y' is a variable that holds the string value "Surendra".  

#THE VARIABLES RULE CRT ORDER#-

#MYVAR="JOHN" #This is correct
#myvar="JOHN" #This is correct
#my-var="JOHN" #This is incorrect because of the hyphen
#my var="JOHN" #This is incorrect because of the space

#THERE ARE MULTIPLE WORDS IN VARIABLE NAMES-
#CAMEL CASE- myVariableName - EACH WORD STARTS WITH A CAPITAL LETTER EXCEPT THE FIRST ONE
#PASCAL CASE- MyVariableName  - EACH WORD STARTS WITH A CAPITAL LETTER
#SNAKE CASE- my_variable_name - EACH WORD IS SEPARATED BY AN UNDERSCORE

#assign multiple values to multiple variables
x,y,z=10,20,30
print(x) # Output: 10
print(y) # Output: 20
print(z) # Output: 30


#one value to multiple variables
x=y=z=10
print(x) # Output: 10
print(y) # Output: 10
print(z) # Output: 10

#unpacking a collection
#if you have a collection of values in a list, tuple, or any other iterable, you can unpack them into individual variables this is called unpacking a collection
fruits=["apple","banana","cherry"]  
x,y,z=fruits
print(x) # Output: apple
print(y) # Output: banana
print(z) # Output: cherry

#output variables
x="python is awesome"
print(x) # Output: python is awesome

x="python"
y="is"
z="awesome" 
print(x,y,z) # Output: python is awesome 0r 
print(x+y+z) # Output: pythonisawesome
