
#                   Built -in Modules in Python

#In Python, built-in modules are pre-installed libraries that come with the Python standard library. These modules provide a wide range of functionalities and can be used without the need for any additional installation. Some commonly used built-in modules in Python include:

#1.math:

#The math module provides mathematical functions such as trigonometric functions, logarithmic functions, and constants like pi and e. For example, we can use the math.sqrt() function to calculate the square root of a number.

import math
result = math.sqrt(16)
print(result) #Output- 4.0 
#explanation- In the above code, we have imported the math module and used the sqrt() function to calculate the square root of 16, which returns 4.0.

#2.Datetime:

#The datetime module provides classes for manipulating dates and times. It allows you to work with dates and times in both simple and complex ways. For example, we can use the datetime.now() function to get the current date and time.

import datetime
current_datetime = datetime.datetime.now()
print(current_datetime) #Output- 2024-06-30 12:34:56.789012
#explanation- In the above code, we have imported the datetime module and used the now() function to get the current date and time, which returns a datetime object representing the current date and time.

#3.os:

#The os module provides a way of using operating system dependent functionality like reading or writing to the file system, interacting with the environment variables, and working with processes. For example, we can use the os.listdir() function to get a list of files and directories in a specified path.

import os
current_directory = os.getcwd()
print(current_directory) #Output- C:\Users\manth\Downloads\python-learning-journey
#explanation- In the above code, we have imported the os module and used the getcwd() function to get the current working directory, which returns a string representing the current directory path.

#4.sys:

#The sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. For example, we can use the sys.argv list to get the command-line arguments passed to a Python script.

import sys
print(sys.argv) #Output- ['script.py', 'arg1', 'arg2']
#explanation- In the above code, we have imported the sys module and printed the sys.argv list, which contains the command-line arguments passed to the script. The first element of the list is the name of the script itself, followed by any additional arguments.

#5.random:

#The random module provides functions for generating random numbers and performing random operations. For example, we can use the random.randint() function to generate a random integer between a specified range.

import random
random_number = random.randint(1, 10)
print(random_number) #Output- A random integer between 1 and 10
#explanation- In the above code, we have imported the random module and used the randint() function to generate a random integer between 1 and 10, which returns a random integer within that range each time the code is executed.


#6.startswith:

#The startswith() method is a built-in string method in Python that checks if a string starts with a specified prefix. It returns True if the string starts with the prefix, and False otherwise. For example:

my_string = "Hello, World!"
print(my_string.startswith("Hello")) #Output- True
print(my_string.startswith("World")) #Output- False
#explanation- In the above code, we have defined a string variable my_string and used the startswith() method to check if it starts with the prefix "Hello" and "World". The first call returns True because my_string does indeed start with "Hello", while the second call returns False because it does not start with "World".


#7.collections:

#The collections module provides alternatives to built-in container data types such as lists, dictionaries, and tuples. It includes specialized data structures like namedtuple, deque, Counter, and defaultdict. For example, we can use the Counter class to count the occurrences of elements in a list.

from collections import Counter
my_list = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
counter = Counter(my_list)
print(counter) #Output- Counter({'apple': 3, 'banana': 2, 'orange': 1})
#explanation- In the above code, we have imported the Counter class from the collections module and used it to count the occurrences of each element in the my_list. The Counter object returned shows that 'apple' occurs 3 times, 'banana' occurs 2 times, and 'orange' occurs 1 time in the list.

#8.json:

#The json module provides functions for working with JSON (JavaScript Object Notation) data. It allows you to parse JSON strings and convert Python objects to JSON format. For example, we can use the json.dumps() function to convert a Python dictionary to a JSON string.

import json
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(my_dict)
print(json_string) #Output- {"name": "Alice", "age": 30, "city": "New York"}
#explanation- In the above code, we have imported the json module and used the dumps() function to convert a Python dictionary my_dict into a JSON string. The resulting JSON string represents the same data as the original dictionary but in a format that can be easily transmitted or stored as text.


#9.re:

#The re module provides functions for working with regular expressions in Python. It allows you to search, match, and manipulate strings based on specific patterns. For example, we can use the re.findall() function to find all occurrences of a pattern in a string.

import re
my_string = "The rain in Spain stays mainly in the plain."
pattern = r'\b\w+ain\b'
matches = re.findall(pattern, my_string)
print(matches) #Output- ['rain', 'Spain', 'plain']
#explanation- In the above code, we have imported the re module and used the findall() function to search for all words in my_string that end with "ain". The regular expression pattern r'\b\w+ain\b' matches any word that starts with a word boundary (\b), followed by one or more word characters (\w+), and ends with "ain" followed by another word boundary. The resulting list matches contains all the words that match this pattern, which are 'rain', 'Spain', and 'plain'.

#10.dir():

#The dir() function is a built-in function in Python that returns a list of the attributes and methods of an object. It can be used to explore the properties and capabilities of an object. For example, we can use the dir() function to see the attributes and methods of a string object.the dir() can be used on all modules , also the ones you create yourself and also on the built-in data types like list , tuple , dictionary etc. For example, we can use the dir() function to see the attributes and methods of a list object.

my_string = "Hello, World!"
attributes_methods = dir(my_string)
print(attributes_methods) #Output- A list of attributes and methods of the string object
#explanation- In the above code, we have defined a string variable my_string and used the dir() function to get a list of all the attributes and methods associated with the string object. The resulting list attributes_methods contains the names of all the attributes and methods that can be accessed or called on the string object, such as 'upper', 'lower', 'split', 'replace', etc. This allows us to explore the functionality available for string objects in Python.
