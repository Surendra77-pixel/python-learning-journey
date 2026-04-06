
#List comprehension------------------------

#1.List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expression can be anything, meaning you can put in all kinds of objects in lists. in simple words , the list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits= ["banana", "apple", "cherry"]
new_fruits = [fruit.upper() for fruit in fruits]
print(new_fruits) #output: ['BANANA', 'APPLE', 'CHERRY']#explanation: In this code, we have a list of fruits with three elements. We use list comprehension to create a new list called new_fruits, where each fruit from the original list is converted to uppercase using the upper() method. The expression fruit.upper() is evaluated for each fruit in the fruits list, and the resulting uppercase strings are collected into the new_fruits list. Finally, we print the new_fruits list, which outputs ['BANANA', 'APPLE', 'CHERRY'].


numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers) #output: [1, 4, 9, 16, 25]
#explanation: In this code, we have a list of numbers from 1 to 5. We use list comprehension to create a new list called squared_numbers, where each number from the original list is squared using the expression number ** 2. The expression number ** 2 is evaluated for each number in the numbers list, and the resulting squared values are collected into the squared_numbers list. Finally, we print the squared_numbers list, which outputs [1, 4, 9, 16, 25].




#2. you can also add a condition to the list comprehension to filter items from the original list. This is done using an if statement after the for clause.

fruits = ["banana", "apple", "cherry", "date", "fig"]
short_fruits = [fruit for fruit in fruits if len(fruit) <= 5]
print(short_fruits) #output: ['apple', 'fig']
#explanation: In this code, we have a list of fruits with five elements. We use list comprehension to create a new list called short_fruits, where we include only those fruits from the original list that have a length of 5 or less. The expression fruit for fruit in fruits iterates through each fruit in the fruits list, and the condition if len(fruit) <= 5 filters out any fruit that does not meet the length requirement. The resulting list short_fruits contains only 'apple' and 'fig', which are the fruits with 5 or fewer characters. Finally, we print the short_fruits list, which outputs ['apple', 'fig'].


numbers = [1, 2, 3, 4, 5]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers) #output: [2, 4]
#explanation: In this code, we have a list of numbers from 1 to 5. We use list comprehension to create a new list called even_numbers, where we include only those numbers from the original list that are even. The expression number for number in numbers iterates through each number in the numbers list, and the condition if number % 2 == 0 filters out any number that is not even. The resulting list even_numbers contains only 2 and 4, which are the even numbers from the original list. Finally, we print the even_numbers list, which outputs [2, 4].

fruits = ["banana", "apple", "cherry", "date", "fig"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist) #output: ['banana', 'apple', 'date']
#explanation: In this code, we have a list of fruits with five elements. We create an empty list called newlist to store the fruits that contain the letter "a". We use a for loop to iterate through each fruit in the fruits list, and we check if the letter "a" is present in each fruit using the condition if "a" in x. If the condition is true, we append the fruit to the newlist using the append() method. Finally, we print the newlist, which outputs ['banana', 'apple', 'date'], as these are the fruits that contain the letter "a".    
 
#now let us see the same method using list comprehension:
fruits = ["banana", "apple", "cherry", "date", "fig"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #output: ['banana', 'apple', 'date']
#explanation: In this code, we have a list of fruits with five elements. We use list comprehension to create a new list called newlist, where we include only those fruits from the original list that contain the letter "a". The expression x for x in fruits iterates through each fruit in the fruits list, and the condition if "a" in x filters out any fruit that does not contain the letter "a". The resulting list newlist contains only 'banana', 'apple', and 'date', which are the fruits that contain the letter "a". Finally, we print the newlist, which outputs ['banana', 'apple', 'date'].



