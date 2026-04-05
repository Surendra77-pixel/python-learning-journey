#pass: The pass statement is a null operation in Python. It is used as a placeholder when a statement is required syntactically but no code needs to be executed. It allows you to create empty blocks of code without causing a syntax error. The pass statement is often used in situations where you want to define a function, class, or loop but haven't implemented the logic yet.


#Example of using pass statement in a function:

age =20
if age >=18:
    pass #output: (no output, the pass statement does nothing)
else:
    print("You are not eligible to vote.") #output: You are not eligible to vote.


#example with pass but the esle block is executed:

age = 16
if age >= 18:
    pass #output: (no output, the pass statement does nothing)
else:
    print("You are not eligible to vote.") #output: You are not eligible to vote..