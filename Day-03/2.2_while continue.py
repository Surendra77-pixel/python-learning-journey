#WHILECONTINUE
#The continue statement is used to skip the current iteration of a loop and move on to the  next iteration. It can be used in both while and for loops. When the continue statement is encountered, the rest of the code inside the loop for that iteration is skipped, and the loop proceeds to the next iteration.

#Example of using continue in a while loop:
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue #output: 1 3 5 7 9
    print(i) 

#REAL-WORLD EXAMPLE
#Let's say we want to print all the odd numbers from 1 to 20, but we want to skip the number 13. We can use the continue statement to achieve this:
i = 1
while i <= 20:
    if i == 13:
        i += 1
        continue #output: 1 3 5 7 9 11 15 17 19
    print(i)
    i += 1 