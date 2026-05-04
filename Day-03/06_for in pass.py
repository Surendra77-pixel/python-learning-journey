
#pass - The pass in the for loop is used as a placeholder for code that will be written later. It allows the loop to run without any code inside it, which can be useful for testing or when you want to create a loop structure but haven't decided on the specific actions to take within the loop yet.

#Example of using pass in a for loop:
from tabnanny import check
for i in range(1, 6):
    pass # This will do nothing and the loop will run indefinitely until we manually stop it. It is important to note that using pass in a for loop without any condition to break the loop can lead to an infinite loop, so it should be used with caution. In this example, the loop will run indefinitely because there is no code to change the value of i or to break the loop.


#Real-world example of using pass in a for loop:


#Let's say we are developing a game and we want to create a loop that will run until the player wins the game. We can use a for loop with a pass statement to create the structure of the loop, and then we can fill in the code later to check for the winning condition.
game_won = False
for _ in range(100): # This loop will run 100 times, but we can replace the range with a while loop if we want it to run indefinitely until the player wins.
    pass # This will do nothing and the loop will run indefinitely until we implement the logic to check for the winning condition. Once we have the logic in place, we can replace the pass statement with the code that checks if the player has won the game and sets game_won to True when they