
#Lambda 

#Lambda functions are anonymous functions that can be defined in a single line of code. They are often used for simple operations that can be expressed in a concise way. The syntax for a lambda function is as follows:

#A small anonymous function that can be delined in a single line of code   


#------------------lambda arguments: expression

#Here, arguments are the input parameters for the function, and expression is the operation that the function performs on those arguments. The lambda function can take any number of arguments, but it can only have one expression.

#Example 1: A lambda function that adds two numbers-

add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

#Example 2: A lambda function that squares a number-

square = lambda x: x ** 2   
print(square(4))  # Output: 16

#Example 3: A lambda function that checks if a number is even-

is_even = lambda x: x % 2 == 0
print(is_even(6))  # Output: True
print(is_even(7))  # Output: False

#Example 4: A lambda function that sorts a list of tuples based on the second element-

my_list = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
my_list.sort(key=lambda x: x[1])
print(my_list)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

#Example 5: A lambda function that filters a list of numbers to include only even numbers-

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

#Example 6: A lambda function that maps a list of numbers to their squares-

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#Example 7: A lambda function that reduces a list of numbers to their product-
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
#In this example, we use the reduce function from the functools module to apply the lambda function that multiplies two numbers across all elements in the list. The result is the product of all the numbers in the list, which is 120 (1 * 2 * 3 * 4 * 5 = 120).

#add 10 to arugument a , and return the result-

x = lambda a: a + 10
print(x(5))  # Output: 15 explanation: In this example, we define a lambda function that takes a single argument a and adds 10 to it. When we call the function with the argument 5, it returns 15 (5 + 10 = 15).


#2.Why use lambda functions?

#Lambda functions are often used in situations where a simple function is needed for a short period of time, and defining a full function using the def keyword would be unnecessary or cumbersome. They are commonly used in conjunction with higher-order functions like map(), filter(), and reduce(), where a function is required as an argument to perform a specific operation on a collection of data. Lambda functions can help to make code more concise and readable by allowing you to define small, one-off functions without the need for a formal function definition. Additionally, lambda functions can be useful for creating simple callbacks or for use in situations where a function is required but defining a full function would be overkill.

def my_func(n):
    return lambda a: a * n
my_doubler = my_func(2)
print(my_doubler(5))  # Output: 10
#In this example, we define a function my_func that takes a single argument n and returns a lambda function that takes another argument a and multiplies it by n. When we call my_func(2), it returns a lambda function that multiplies its argument by 2. We assign this lambda function to the variable my_doubler. When we call my_doubler(5), it multiplies 5 by 2 and returns 10. This demonstrates how lambda functions can be used to create simple, reusable functions on the fly without the need for a formal function definition.

#or use the same function defination to make a function that always triples the number you send in 

def my_fun(n):
    return lambda a: a * n
my_tripler = my_fun(3)
print(my_tripler(11))  # Output: 33 

#or use the same function defination to make both functions in the same program-

def my_fun(n):
    return lambda a: a * n
my_doubler = my_fun(2)
my_tripler = my_fun(3)
print(my_doubler(11))  # Output: 22
print(my_tripler(11))  # Output: 33


#Builtin functions that use lambda functions-

#1. map() -

#  The map() function applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator). You can use a lambda function as the first argument to map() to perform a specific operation on each item in the iterable.

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
#In this example, we use the map() function to apply a lambda function that squares each number in the list. The result is a new list of squared numbers.

#2. filter() -

#  The filter() function constructs an iterator from elements of an iterable for which a function returns true. You can use a lambda function as the first argument to filter() to specify the condition that each item in the iterable must satisfy.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
#In this example, we use the filter() function to apply a lambda function that checks if each number in the list is even. The result is a new list of even numbers.

numbers = [1 ,2 , 3 , 4 , 5 , 6 , 7 ,8 ]
def even_numbers(num):
    return num % 2 == 0 
even_num=tuple(filter(even_numbers,numbers))
print(even_num) # Output: (2, 4, 6, 8) - In this example, we define a function even_numbers that takes a number as an argument and returns True if the number is even (i.e., divisible by 2 with no remainder) and False otherwise. We then use the filter() function to apply this function to each element in the numbers list. The result is a new tuple containing only the even numbers from the original list, which are (2, 4, 6, 8).


#3. reduce() -

#  The reduce() function from the functools module applies a rolling computation to sequential pairs of values in an iterable. You can use a lambda function as the first argument to reduce() to specify the operation that should be applied to the items in the iterable.

from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
#In this example, we use the reduce() function to apply a lambda function that multiplies two numbers across all elements in the list. The result is the product of all the numbers in the list, which is 120 (1 * 2 * 3 * 4 * 5 = 120).   


#4.sorted() -

#  The sorted() function returns a new sorted list from the items in an iterable. You can use a lambda function as the key argument to specify a function of one argument that is used to extract a comparison key from each element in the iterable.

my_list = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
#In this example, we use the sorted() function to sort a list of tuples based on the second element of each tuple (the fruit name). The lambda function takes each tuple x and returns the second element x[1] as the key for sorting. The result is a new list of tuples sorted by the fruit names in alphabetical order.  




