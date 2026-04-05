#WHILE BREAK

#The break statement is used to exit a loop prematurely when a certain condition is met. It can be used in both while and for loops. When the break statement is encountered, the loop is immediately terminated and the program continues with the next statement after the loop.  

#Example of using break in a while loop:
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break #output: 1 2 3 4 5
    i += 1  

#REAL LIFE EXAMPLE OF USING BREAK IN A WHILE LOOP:
#Imagine you are playing a game where you have to guess a number between 1 and 10. You keep guessing until you find the correct number. Once you find the correct number, you want to stop guessing and end the game. In this case, you can use a while loop to keep asking for guesses and a break statement to exit the loop when the correct number is guessed.

#Example of using break in a while loop for a guessing game:
import random
number_to_guess = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number_to_guess:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")

#