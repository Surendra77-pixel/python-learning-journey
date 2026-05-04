#built-in functions in Python - 

# Built-in functions are functions that are provided by Python and are available for use without the need for importing any additional modules. These functions perform a wide range of tasks, such as manipulating data, performing calculations, and working with different data types.

#1.print()
# The print() function is used to display output to the console. It can take multiple arguments and will convert them to strings before printing them. You can also specify a separator between the arguments using the sep parameter and end the output with a specific character using the end parameter.
print("Hello, World!") #output: Hello, World!
print("Hello", "World", sep="-") #output: Hello-World
print("Hello", end=" ") #output: Hello


#2.input() - 
# The input() function is used to take input from the user. It displays a prompt to the user and waits for them to enter some data. The input is returned as a string.
name = input("Enter your name: ")
print("Hello, " + name + "!") #output: Hello, [name]!


#3.len() -
# The len() function is used to get the length of an object, such as a string, list, or tuple. It returns the number of items in the object.
my_string = "Hello, World!"
print(len(my_string)) #output: 13

my_list = [1, 2, 3, 4, 5]
print(len(my_list)) #output: 5

#4.type() -
# The type() function is used to get the type of an object. It returns the type of the object as a string.
my_string = "Hello, World!"
print(type(my_string)) #output: <class 'str'>

my_list = [1, 2, 3, 4, 5]
print(type(my_list)) #output: <class 'list'>


#5.int(), float(), str() -
# The int(), float(), and str() functions are used to convert values to integers, floating point numbers, and strings, respectively. They take a single argument and return the converted value.
my_string = "123"
my_int = int(my_string)
print(my_int) #output: 123

my_float = float(my_string)
print(my_float) #output: 123.0

my_number = 123
my_string = str(my_number)
print(my_string) #output: '123'


#6.bool() -
# The bool() function is used to convert a value to a boolean (True or False). It takes a single argument and returns True if the value is truthy and False if the value is falsy.
print(bool(0)) #output: False
print(bool(1)) #output: True
print(bool("")) #output: False
print(bool("Hello")) #output: True


#7.range() -
# The range() function is used to generate a sequence of numbers. It takes three arguments: start, stop, and step. The start argument is the starting number of the sequence (inclusive), the stop argument is the ending number of the sequence (exclusive), and the step argument is the increment between each number in the sequence.
for i in range(5):
    print(i) #output: 0 1 2 3 4

for i in range(1, 10, 2):
    print(i) #output: 1 3 5 7 9


#8.sum() -
# The sum() function is used to calculate the sum of a sequence of numbers. It takes an iterable (such as a list or tuple) as an argument and returns the total sum of the numbers in that iterable.
numbers = [1, 2, 3, 4, 5]
print(sum(numbers)) #output: 15


#9.max() and min() -
# The max() and min() functions are used to find the maximum and minimum values in a sequence of numbers. They take an iterable as an argument and return the maximum or minimum value in that iterable.
numbers = [1, 2, 3, 4, 5]
print(max(numbers)) #output: 5
print(min(numbers)) #output: 1


#10.abs() -
# The abs() function is used to get the absolute value of a number. It takes a single argument and returns the non-negative value of that number.
print(abs(-5)) #output: 5
print(abs(5)) #output: 5


#11.round() -
# The round() function is used to round a number to a specified number of decimal places. It takes two arguments: the number to be rounded and the number of decimal places to round to (optional). If the second argument is not provided, it rounds to the nearest integer.
print(round(3.14159, 2)) #output: 3.14
print(round(3.14159)) #output: 3


#12.sorted() -
# The sorted() function is used to sort a sequence of items. It takes an iterable as an argument and returns a new sorted list of the items in that iterable.
numbers = [5, 2, 9, 1, 5, 6]
print(sorted(numbers)) #output: [1, 2, 5, 5, 6, 9]



#13.reversed() -
# The reversed() function is used to reverse the order of a sequence of items. It takes an iterable as an argument and returns an iterator that produces the items in reverse order.
numbers = [1, 2, 3, 4, 5]
print(list(reversed(numbers))) #output: [5, 4, 3, 2, 1]

#point to rember .reverse is used in the list the reversed() is a built in function that can be used with any iterable. The reverse() method is specific to lists and modifies the list in place, while the reversed() function returns an iterator that can be used with any iterable and does not modify the original object. 


#14/list() , tuple(), set() -
# The list(), tuple(), and set() functions are used to create new lists, tuples, and sets, respectively. They take an iterable as an argument and return a new object of the specified type containing the items from that iterable.
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list) #output: [1, 2, 3]


#15.help() -
# The help() function is used to get information about a function, class, or module.
print(help(print)) #output: Help on built-in function print in module builtins:.

#16.pow() -
# The pow() function is used to calculate the power of a number. It takes two arguments: the base and the exponent, and returns the result of base raised to the power of exponent.
print(pow(2, 3)) #output: 8
print(pow(2, 4)) #output: 16


#16.zip() -
# The zip() function is used to combine two or more iterables into a single iterable of tuples. It takes multiple iterables as arguments and returns an iterator that produces tuples containing the corresponding elements from each iterable.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped)) #output: [(1, 'a'), (2, 'b'), (3, 'c')]


#17.map() -
# The map() function is used to apply a function to each item in an iterable. It takes a function and an iterable as arguments and returns an iterator that produces the results of applying the function to each item in the iterable.
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result)) #output: [2, 4, 6, 8]


#18.filter() -
# The filter() function is used to filter items in an iterable based on a specified condition. It takes a function and an iterable as arguments and returns an iterator that produces the items from the iterable for which the function returns True.
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result)) #output: [2, 4]


#19.any() and all() -
# The any() function returns True if at least one element of the iterable is true, while the all() function returns True if all elements of the iterable are true. They take an iterable as an argument and return a boolean value.
numbers = [0, 1, 2, 3]  
print(any(numbers)) #output: True
print(all(numbers)) #output: False
#explanation: The any() function returns True because there is at least one non-zero element in the list (1, 2, 3). The all() function returns False because not all elements in the list are non-zero (0 is considered false).


#20.type() checking -
# The type() function can also be used to check the type of an object. It returns the type of the object as a string, which can be useful for debugging and ensuring that your code is working with the expected data types.
my_string = "Hello, World!"
print(type(my_string)) #output: <class 'str'>



#isinstance() -
# The isinstance() function is used to check if an object is an instance of a specific class or a subclass thereof. It takes two arguments: the object to check and the class (or tuple of classes) to check against. It returns True if the object is an instance of the specified class or a subclass, and False otherwise.
my_string = "Hello, World!"
print(isinstance(my_string, str)) #output: True
print(isinstance(my_string, int)) #output: False



