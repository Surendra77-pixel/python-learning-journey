
#                      List comprehension 

#The lsit comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, while optionally filtering items using a condition. The syntax for list comprehension is as follows:

#new_list = [expression for item in iterable if condition]

#1. The expression is evaluated for each item in the iterable, and the resulting value is added to the new list. For example, if we want to create a list of squares of numbers from 0 to 9, we can use the following list comprehension:

squares = [x**2 for x in range(10)]
print(squares)
#Output-
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#2. We can also use an if condition to filter items from the iterable. For example, if we want to create a list of even numbers from 0 to 9, we can use the following list comprehension:
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
#Output-
#[0, 2, 4, 6, 8]
