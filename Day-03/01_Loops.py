
#loops - repeated execution of a block of code while a condition is true   AND loops help us to avoid writing the same code again and again

#there are two types of loops in python:
#1. while loop
#2. for loop

#while loop: A while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. The loop will continue to execute as long as the condition is true.

#real life example of while loop:while you are hungry, you will eat food. Once you are full, you will stop eating.

#example of while loop:
i = 1
while i <= 5:
    print(i)
    i += 1 #output: 1 2 3 4 5

#for loop : A for loop is a control flow statement that allows code to be executed repeatedly based on a sequence (like a list, tuple, string) or other iterable object. It iterates over the items of the sequence and executes the block of code for each item.

#real life example of for loop: when you are filling the water bottle, you will fill it until it is full. Once it is full, you will stop filling it . here you when its going to full so give a particular number of times you want to fill the water bottle.

#example of for loop:
for i in range(1, 6):
    print(i) #output: 1 2 3 4 5 .