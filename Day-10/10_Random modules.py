
#                    Random module in Python

#1. The random module in Python is a built-in module that provides functions for generating random numbers and performing random operations. It includes functions for generating random integers, floating-point numbers, and selecting random elements from a sequence.

#2. To use the random module, you need to import it at the beginning of your Python script. This allows you to access the functions and variables defined in the random module.

import random

#3. Some common functions provided by the random module include:

#1.randint():

#The random.randint() function generates a random integer between a specified range. For example, random.randint(1, 10) will return a random integer between 1 and 10 (inclusive).

random_integer = random.randint(1, 10)


#2.random():

#The random.random() function generates a random floating-point number between 0.0 and 1.0. For example, random.random() will return a random float between 0.0 and 1.0.

random_float = random.random()


#3.choice():

#The random.choice() function selects a random element from a non-empty sequence. For example,  random.choice(['apple', 'banana', 'cherry']) will return a random element from the list ['apple', 'banana', 'cherry'].

random_element = random.choice(['apple', 'banana', 'cherry'])


#4.shuffle():

#The random.shuffle() function shuffles the elements of a list in place. For example, random.shuffle(my_list) will shuffle the elements of the list my_list randomly.
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)


#5.sample():

#The random.sample() function returns a specified number of unique elements from a sequence. For example, random.sample([1, 2, 3, 4, 5], 3) will return a list of 3 unique random elements from the list [1, 2, 3, 4, 5].
random_sample = random.sample([1, 2, 3, 4, 5], 3)

