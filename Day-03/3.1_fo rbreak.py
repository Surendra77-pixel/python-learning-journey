#break -The break statement is used to exit a loop prematurely when a certain condition is met. It can be used in both for and while loops. When the break statement is executed, the loop is immediately terminated, and the program continues with the next statement after the loop.

#for loop with break statement:
for i in range(1, 11):
    print(i)
    if i == 5:
        break #output: 1 2 3 4 5
#explanation: In this code, we have a for loop that iterates through the numbers from 1 to 10. Inside the loop, we print the current number (i). We then check if i is equal to 5. If it is, we execute the break statement, which immediately exits the loop. As a result, the loop will only print the numbers 1 through 5 before terminating.

#other example of using break in a for loop:
fruits = ["apple", "banana", "cherry", "date", "fig"]
for fruit in fruits:
    print(fruit)
    if fruit == "cherry":
        break #output: apple banana cherry
#explanation: In this code, we have a for loop that iterates through a list of fruits. Inside the loop, we print the current fruit. We then check if the current fruit is "cherry". If it is, we execute the break statement, which immediately exits the loop. As a result, the loop will only print "apple", "banana", and "cherry" before terminating.

