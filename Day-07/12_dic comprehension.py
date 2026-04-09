
#dictionary comprehension

# We can use dictionary comprehension to create a new dictionary by applying an expression to each item in an iterable. Here is an example:
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}
print(squared_dict) #output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} - The dictionary comprehension iterates over each number in the list numbers and creates a new dictionary called squared_dict where each key is the number itself and the corresponding value is the square of that number. When we print squared_dict, it shows the resulting dictionary with numbers as keys and their squares as values.

# We can also use an if condition in dictionary comprehension to filter items. Here is an example:
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers if num % 2 == 0}
print(squared_dict) #output: {2: 4, 4: 16} - The dictionary comprehension iterates over each number in the list numbers and includes only those numbers that are even (i.e., num % 2 == 0). For each even number, it creates a key-value pair in the squared_dict where the key is the number itself and the value is the square of that number. When we print squared_dict, it shows a dictionary containing only the even numbers as keys and their squares as values.

