#continue - The continue statement is used to skip the current iteration of a loop and move on to the next iteration. It is often used in conjunction with an if statement to skip certain iterations based on a condition. 

#example of using continue in a for loop:
for i in range(1, 11):
    if i % 2 == 0:
        continue #output: 1 3 5 7 9
    print(i)    
#explanation: In this code, we have a for loop that iterates through the numbers from 1 to 10. Inside the loop, we check if the current number (i) is even by using the modulus operator (%). If i is even (i % 2 == 0), we execute the continue statement, which skips the rest of the code inside the loop for that iteration and moves on to the next iteration. As a result, only odd numbers (1, 3, 5, 7, 9) are printed.

#other example of using continue in a for loop:
fruits = ["apple", "banana", "cherry", "date", "fig"]
for fruit in fruits:
    if fruit == "cherry":
        continue #output: apple banana date fig
    print(fruit)
#explanation: In this code, we have a for loop that iterates through a list of fruits. Inside the loop, we check if the current fruit is "cherry". If it is, we execute the continue statement, which skips the rest of the code inside the loop for that iteration and moves on to the next iteration. As a result, "cherry" is not printed, and only "apple", "banana", "date", and "fig" are printed.
