
#The tuple methods -----------------------------

#The tuple data type has several built-in methods that allow us to perform various operations on tuples. Here are some of the commonly used tuple methods:

#1.count() -
 
# The count() method is used to count the number of occurrences of a specified value in a tuple. It takes one argument, which is the value to be counted, and returns the number of times that value appears in the tuple. Here is an example:
my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2)) #output: 3 - The count() method is called on the tuple my_tuple with the argument 2. It counts the number of times the value 2 appears in the tuple, which is 3, and returns that count.   



#2.index() -

#  The index() method is used to find the index of the first occurrence of a specified value in a tuple. It takes one argument, which is the value to be searched for, and returns the index of the first occurrence of that value in the tuple. If the value is not found, it raises a ValueError. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3)) #output: 2 - The index() method is called on the tuple my_tuple with the argument 3. It searches for the value 3 in the tuple and returns the index of its first occurrence, which is 2 (since indexing starts at 0). If we were to search for a value that is not in the tuple, such as 6, it would raise a ValueError.

