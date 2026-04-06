#loops - lists-----------------------




# Loop through a list - You can use a for loop to iterate through the items of a list. The for loop will execute a block of code for each item in the list.
fruits = ["banana", "apple", "cherry"]
for fruit in fruits:
    print(fruit)
#output:
#banana
#apple
#cherry

#1.2.using while loop to loop through a list - You can also use a while loop to iterate through the items of a list. The while loop will execute a block of code as long as a certain condition is true.
fruits = ["banana", "apple", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
#output:
#banana
#apple
#cherry

#2.loop through the index number of a list - You can use the range() function to loop through the index numbers of a list. The range() function generates a sequence of numbers, which can be used to access the items of the list by their index.
fruits = ["banana", "apple", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])
#output:
#banana
#apple
#cherry


#3.looping through the list comprehension - List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expression can be anything, meaning you can put in all kinds of objects in lists.
fruits = ["banana", "apple", "cherry"]
[print(fruit) for fruit in fruits]
#output:
#banana
#apple
#cherry


